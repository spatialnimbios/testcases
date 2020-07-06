%INPUTS: 
% 1. PUtraj: Nx2 vector of the Phosphorylated As (Ap), then
   %     Unphosphorylated As (Au). Assumes first data point is at t=0 (line 140)
% 2. lag_time: (s) time between each datapt in AP.
%
% 3. NchunkInput: Integer, number of chunks to split the trajectory into to collect a standard deviation on residence times.
%State 1 is the low Phosphorylated state (low Ap, high Au)
%State 2 is the high Phosphorylated state (high Ap, low Au)
%In this version, create a transition region, to reduce the number of rapid switches between state 1 and state 2 from a single line
%OUTPUTS:
%stateid: LX1 vector, where L=length(PUtraj), of state assignments for each
%point

%probvec: 2x1 : prob of being in state 1 and state2
%ptrans: 2x2 : transition matrix between states 1 and 2
%TIME STORE CONTAINS: timePerState, timeAvg, timeStd,ntrans,
%timePerState: 2x1: Times (s) spent in each state, calculated from
%transition matrix, depends on lagtime between each pt in AP.
%timeAvg: times (s) spent in each state, calculated as average over all 
%all intervals spent in state 1 vs state 2
%timeStd: stdev of times spent in each state, calculated based on vector
%used to calculate timeAvg. Units of (s)
%ntrans: number of transitions used to calculate timeAvg
%ProbMat: Nchunk x 2: prob of being in S1 or S2, for each chunk of traj.
%MeanPeq: 2x1: avg prob of S1 S2
%SEMpeq: Std(prob S1 and S2)/sqrt(Nchunks).

function[stateid,  probvec, ptrans,TIMESTORE,ntrans,  ProbMat, MeanPeq, SEMPeq]=assign_states_upThresh(PUtraj, lag_time, NchunkInput)
T=length(PUtraj)
stateid=zeros(T,1);

%define lines for the high and low state, and transition region.
icept1=62; %empirical choice based on boundary of state 1

m=1;%for both lines, slope of 1 is good.

icept2=35; %empirical choice based on boundary of state 2

%CREATE transition region. 
for i=1:T
    %AU > 62+ Ap
    if(PUtraj(i,2)>icept1+PUtraj(i,1)*m )
        stateid(i)=1; %kinase is mostly unphosphorylated.
    elseif(PUtraj(i,2)<icept2+PUtraj(i,1)*m)
        stateid(i)=2; %AU < 35+ Ap
    else
        %In the transition region, decide which state based on previous
        %state!
        if(stateid(i-1)==1)stateid(i)=1;
        else
            stateid(i)=2;
        end
    end
end
index1=find(stateid==1);

index2=find(stateid==2);
Nstate1=length(index1);
Nstate2=length(index2);
%prob of being in each state
p1=Nstate1/(Nstate1+Nstate2)
p2=Nstate2/(Nstate1+Nstate2)
probvec=[p1;p2]

  fignum=1;
f3=figure(fignum+3)
h3=histogram2(PUtraj(:,1),PUtraj(:,2));
xval=h3.XBinEdges(1:end-1)+h3.BinWidth(1)*0.5
yval=h3.YBinEdges(1:end-1)+h3.BinWidth(2)*0.5
ff=figure(fignum+4)
ax=axes('Parent',ff,'FontSize',20,'LineWidth',1,'XScale','linear','YScale','linear')
hold(ax)

surf(xval, yval, h3.Values')
xlabel('Ap copies')
ylabel('Unphosphorylated copies')
x=[0:1:40];
y=x+icept1;
y2=x+icept2;
z=ones(length(y),1)*2000;%it won't be visible unless it is above the surfaces
plot3(x, y, z,'r-','LineWidth',5)
plot3(x, y2,z,'m-','LineWidth',5)

%transition probabilities 1-1, 1-2, 2-1, 2-2
d=diff(stateid);
p12=length(find(d>0));
p21=length(find(d<0));
id1=find(d==0);
pstay=length(id1);
p11=length(find(stateid(id1+1)==1)); %diff start at x(2)-x(1), so index1 of the id1 vector corresponds to transition from i1->i2
p22=length(find(stateid(id1+1)==2));

ntransMat=[p11, p12 ; p21, p22]
ptrans=[ p11/(p11+p12), p12/(p11+p12) ; p21/(p21+p22), p22/(p21+p22)]


%find interval lengths spent in state 1
ival1=find(diff(index1)~=1);
ival2=find(diff(index2)~=1);
%above differences ignore the first and last intervals. To add them:
ival1=[0;ival1;length(index1)];
ival2=[0;ival2;length(index2)];

steps1=diff(ival1); %this is a vector of interval lengths
steps2=diff(ival2);
steps1=steps1*lag_time;
steps2=steps2*lag_time;
minIntTime=min(min(steps1), min(steps2))
maxIntTime=max(max(steps1), max(steps2))
tvals=logspace(log10(minIntTime), log10(maxIntTime), 20);

f1=figure(fignum+1);
h=histogram(steps1, tvals)

figure(fignum+2)
h2=histogram(steps2, tvals)
timeAvg=[mean(steps1); mean(steps2)]; %average time in sec for each state
timeStd=[std(steps1); std(steps2)];
ntrans=[length(steps1); length(steps2)]%number of transitions out of state 1 and state 2

timePerState=-1./diag(logm(ptrans)/lag_time);
%To get kth powers of ptrans:
[v,d,w]=eig(ptrans);
k=10 %which power to take
ptransk10=inv(v*w')*v*d^k*w' % this matrix should approx match if you calculated ptrans at k*lag_time

timePerStatek10=-1./diag(logm(ptransk10)/(lag_time*k));%over 10 times less frequent.
%steady state is left eignevector where eigenvalue=1. 
pss=find(diag(d)==1);
eig_ss=w(:,pss);
%normalize the SS
peq=eig_ss/sum(eig_ss)



f=figure(fignum)
ax=axes('Parent',f,'FontSize',20,'LineWidth',1,'XScale','linear','YScale','linear')
hold(ax)

timevec=[0:lag_time:(T-1)*lag_time];%assumes first time-pt is Zero!

plot(timevec, PUtraj(:,2),'b--','LineWidth',2)

plot(timevec(index1), PUtraj(index1,1),'ro','LineWidth',2); %State 1 pts
plot(timevec(index2), PUtraj(index2,1),'y+','LineWidth',2) %State 2 pts (HIgh)
plot(timevec, PUtraj(:,1),'k-','LineWidth',2)
legend('Au','Low phos state','High phos state','Ap')

xlabel('time (s)')
ylabel('Copies')


%split traj into nchunks, calculate probs for each chunks
chunkTime=max(timeStd);%approx block size where residence is decorrelated.
maxTime=T*lag_time; %time of simulation
Ntimechunk=maxTime/chunkTime;% If this is very large, don't need that much.
Nchunk=min(NchunkInput, round(Ntimechunk));%If Ntimechunk is large, just use ~10 or so blocks is enough!
if(Nchunk<2)
    display('WARNING, trajectory is not long enough to calculate statistics on state probabilities!') 
end
display('N chunks to quantify probabilities: ')
Nchunk
ptsPer=round(T/Nchunk);
ProbMat=zeros(2, Nchunk);%Nstates=2, by Nchunks
for i=1:1:Nchunk
    id1=(i-1)*ptsPer+1;
    id2=id1+ptsPer-1;
    if(id2>T)id2=T; end
    chunk=stateid(id1:id2);
    
    c11=find(chunk==1);

    %prob of being in each state
    chunkp1=length(c11)/length(chunk);
    chunkp2=1-chunkp1;
    ProbMat(1,i)=chunkp1;
    ProbMat(2,i)=chunkp2;
end

%Average state probabilities, over Nchunks
MeanPeq=mean(ProbMat')';
%Std of state probabilities, over Nchunks
SEMPeq=std(ProbMat')'/sqrt(Nchunk);

TIMESTORE=[timePerState, timeAvg, timeStd];
