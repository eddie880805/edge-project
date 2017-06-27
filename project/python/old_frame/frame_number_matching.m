function [output]=frame_number_matching(In)
%number matching only
%initial, MER AND SD has inverse relation of perference, so we add ""-" 
MER=0;
NAV=0;
SD=0;
R2=0;
YIELD=0;
I=[MER,NAV,SD,R2,YIELD];
%s1 size of investor input
s1=size(I);


%input example

%input data
%manager now we only have midian class
manager=zeros(200,s1(2));

sm=size(manager);




for j=1:sm(1)
    for i=1:s1(2)
    %generate 6 random number from 0 to 10
    rng('shuffle');
    a = 0;
    b = 10;
    r = (b-a).*rand(s1(2),1) + a;
    manager(j,i)=r(i);
    if i==1
        manager(j,i)=-manager(j,i);
    elseif i==3
        manager(j,i)=-manager(j,i);
    end
    end
end
        


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

matching_n=zeros(sm);



matching_list_n=[];
% c control rating
c=4/5;

for i=1:sm(1)
    for j=1:s1(2)
        if manager(i,j)>=In(j)
            matching_n(i,j)=1;
        else
            matching_n(i,j)=0;
        end
        
    end
    if sum(matching_n(i,:))>=c*s1(2)
        matching_list_n=[matching_list_n,i];
    end

    
end

output=matching_list_n;

end

      
%matching_i return M1 satisfies In input.
