%question1 A-E

%question2 A-C

%question3 A-D

%question4-9 

%question10-15 

%typital example
%I=[Q1,Q2,Q3,Q49,Q1015];
I=["E","C","D",51,51];

allocation=[];
if I(1)=="A" && I(3)=="A" && double(I(5))<20
   allocation=[allocation,"very conservative"];
elseif I(1)=="B" && I(3)=="B" && double(I(4))<15 ...
    && double(I(5))>=20 && double(I(5))<=24
    allocation=[allocation,"conservative income"];
elseif I(2)=="A" && I(3)=="C" && double(I(4))>=15 ...
    && double(I(4))<=25 && double(I(5))>=25 ...
    && double(I(5))<=30
    allocation=[allocation,"balanced"];
elseif (I(1)=="C" || I(1)=="D") && I(2)=="B" ...
        && double(I(4))>=26 && double(I(4))<=40 ...
        && double(I(5))>=31 && double(I(5))<=45
    allocation=[allocation,"grwoth"];
elseif I(1)=="E" && I(2)=="C" && I(3)=="D" ...
        && double(I(4))>40 && double(I(5))>45
    allocation=[allocation,"aggresive growth"];

end



