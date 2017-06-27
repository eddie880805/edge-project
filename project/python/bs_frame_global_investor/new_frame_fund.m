clear all
[num,txt,raw] = xlsread('text.xls');

[row,col]=size(raw);

for r=1:row
    raw{r,9}=str2double(raw{r,9});
    raw{r,8}=str2double(raw{r,8});
    raw{r,7}=str2double(raw{r,7});
    raw{r,6}=str2double(raw{r,6});
    raw{r,5}=str2double(raw{r,5});
    raw{r,4}=str2double(raw{r,4});
    raw{r,2}=strrep(raw{r,2},'$','');
    raw{r,2}=str2double(raw{r,2});
    raw{r,1}=strrep(raw{r,1},'%','');
    raw{r,1}=str2double(raw{r,1});
    
    raw{r,3}=strrep(raw{r,3},'%','');
    if contains(raw{r,3},'m')
        raw{r,3}=strrep(raw{r,3},'m','');
    end
    raw{r,3}=str2double(raw{r,3});
   
   
end



% 
% return/price/MER/risk and beta
I=[3.5,11,2,6,5,4,3,2,1,"Open-Ended","",""];




%if matching exist

for r=1:row
    if ~isnan(raw{r,1}) && ~isnan(raw{r,2}) && ~isnan(raw{r,3})...
        && ~isnan(raw{r,4}) && ~isnan(raw{r,5}) && ~isnan(raw{r,6})...
        && ~isnan(raw{r,7}) && ~isnan(raw{r,8}) && ~isnan(raw{r,9})
            if str2double(I(1))<=raw{r,1}...
                    && str2double(I(2))>=raw{r,2}...
                    && str2double(I(3))>=raw{r,3}...
                    && str2double(I(4))>=raw{r,4}...
                    && str2double(I(5))>=raw{r,5}...
                    && str2double(I(6))>=raw{r,6}...
                    && str2double(I(7))>=raw{r,7}...
                    && str2double(I(8))>=raw{r,8}...
                    && str2double(I(9))>=raw{r,9}...

                raw(r,11)
            end
    end
end
%did not consider missing data



%if matching DNE
%-we find the closest match

%if multiple matching exist
%-we rank

%algorithm
    


