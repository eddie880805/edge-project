function [output]=frame_multiple_string_matching(Is)
%number matching only
%initial, MER AND SD has inverse relation of perference, so we add "-" 



ACCOUNT_TYPE = {'at1';'at2';'at3';'at4';'NA';'NA'};
REGION = {'r1';'r2';'r3';'r4';'NA';'NA'};
STYLE = {'s1';'s2';'s3';'s4';'NA';'NA'};
FOCUS={'f1';'f2';'f3';'f4';'NA';'NA'};
RISK={'H';'MH';'M';'ML';'L';'NA'};



w_ACCOUNT_TYPE=0.2;
w_REGION=0.1;
w_STYLE=0.2;
w_FOCUS=0.1;
w_RISK=0.4;
weight_list=[w_ACCOUNT_TYPE,w_REGION,w_STYLE,w_FOCUS,w_RISK];

M=[ACCOUNT_TYPE,REGION,STYLE,FOCUS,RISK];
sM=size(M);

%input sample
sI=size(Is);


matching_s=zeros(sM);

matching_list_s=[];


%find not Na element
counting_not_NA=zeros(1,sM(2));

for i=1:sM(2)
    for j=1:sM(1)
        if strcmp(M(j,i),'NA')==0
            counting_not_NA(1,i)=counting_not_NA(1,i)+1;
        end
    end
end

for i=1:sI(2)
    for k=1:sM(2)
        for j=1:sM(1)
            if strcmp(Is(i),M(j,k))==1
                matching_s(j,k)=1;
            end
            
        end

    end
     
end

%find weight

counting_one=zeros(1,sM(2));


for i=1:sM(2) 
    counting_one(1,i)=sum(matching_s(:,i));
end
    
percentage_list=counting_one./counting_not_NA; 


final_weight_s=0;
for i=1:sM(2)
    weight=weight_list(i)*percentage_list(i);
    final_weight_s=final_weight_s+weight;
end

output=final_weight_s;
end


