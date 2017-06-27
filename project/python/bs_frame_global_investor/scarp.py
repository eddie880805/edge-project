from bs4 import BeautifulSoup
import urllib.request
import xlwt
import xlrd
import lxml
import re

base_url = "https://secure.globeadvisor.com/gi/db/gaf.fund_pro?fundname="


fund_list=["Aurion+Canadian+Equity+Fund&pi_universe=PUBLIC_FUND",
"Aurion+Income+Opportunities+Fd+Cl+A&pi_universe=PUBLIC_FUND",
"Aurion+Income+Opportunities+Fd+Cl+F&pi_universe=PUBLIC_FUND",
"LOGiQ+Select+Equity+Fund+Series+A&pi_universe=PUBLIC_FUND",
"LOGiQ+Select+Equity+Fund+Series+F&pi_universe=PUBLIC_FUND",
"Scotia+Institutional+Tactical+Bond&pi_universe=PUBLIC_FUND",
"ABC+American-Value&pi_universe=PUBLIC_FUND",
"ABC+Fully-Managed&pi_universe=PUBLIC_FUND",
"ABC+Fundamental+Value&pi_universe=PUBLIC_FUND",
"Acker+Finley+Select+Canada+Focus+A&pi_universe=PUBLIC_FUND",
"Acker+Finley+Select+Canada+Focus+F&pi_universe=PUBLIC_FUND",
"Acker+Finley+Select+US+Value+50+A&pi_universe=PUBLIC_FUND",
"Acker+Finley+Select+US+Value+50+F&pi_universe=PUBLIC_FUND",
"ACM+Commercial+Mtg+Cl+F&pi_universe=PUBLIC_FUND",
"Acorn+Diversified+Trust&pi_universe=PUBLIC_FUND",
"ReSolve+Adaptive+Asset+Allocation+A&pi_universe=PUBLIC_FUND",
"ReSolve+Adaptive+Asset+Allocation+F&pi_universe=PUBLIC_FUND",
"AGF+Diversified+Inc+Cl+Srs+Q&pi_universe=PUBLIC_FUND",
"AGF+Diversified+Income+-Q&pi_universe=PUBLIC_FUND",
"AGF+Diversified+Income+Srs+Q&pi_universe=PUBLIC_FUND",
"AGF+Fixed+Income+Plus+Srs+Q&pi_universe=PUBLIC_FUND",
"AGF+Tactical+Income+-Q&pi_universe=PUBLIC_FUND",
"Agilith+North+American+Diversified&pi_universe=PUBLIC_FUND",
"Enhanced+Inc+Fin+ETF+Advs+Cl&pi_universe=PUBLIC_FUND",
"HAP+Balanced+ETF&pi_universe=PUBLIC_FUND",
"HAP+Corporate+Bond+ETF&pi_universe=PUBLIC_FUND",
"HAP+Enhanced+Income+Equity+ETF&pi_universe=PUBLIC_FUND",
"HAP+Enhanced+Income+Equity+ETF+Adv&pi_universe=PUBLIC_FUND",
"HAP+Floating+Rate+Bond+ETF&pi_universe=PUBLIC_FUND",
"HAP+Floating+Rate+Bond+ETF+Advisor&pi_universe=PUBLIC_FUND",
"HAP+Gartman&pi_universe=PUBLIC_FUND",
"HAP+Income+Plus+ETF-E&pi_universe=PUBLIC_FUND",
"HAP+North+American+Value+ETF&pi_universe=PUBLIC_FUND",
"HAP+S%26P%2FTSX+60EqWgIdx&pi_universe=PUBLIC_FUND",
"Horizons+Absolute+Rtn+Glo+Curr+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Act+Cdn+Bd+ETF+Adv+Cl&pi_universe=PUBLIC_FUND",
"Horizons+Act+Cdn+Div+ETF+AdvCl&pi_universe=PUBLIC_FUND",
"Horizons+Act+Cdn+Mcpl+Bd+ETF+Adv+Cl&pi_universe=PUBLIC_FUND",
"Horizons+Act+Cdn+Mcpl+Bd+ETF+Cl+E&pi_universe=PUBLIC_FUND",
"Horizons+Act+EM+Div+ETF+Adv+Cl&pi_universe=PUBLIC_FUND",
"Horizons+Act+HY+Bd+ETF+AdvCl&pi_universe=PUBLIC_FUND",
"Horizons+Active+Cdn+Bond+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Active+Cdn+Dividend+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Active+Corp+Bond+ETF+Adv&pi_universe=PUBLIC_FUND",
"Horizons+Active+Diversified+Inc+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Active+EM+Div+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Active+Glbl+FI+ETF+Advs+Cl&pi_universe=PUBLIC_FUND",
"Horizons+Active+Global+Divi+ETF+Adv&pi_universe=PUBLIC_FUND",
"Horizons+Active+Global+Dividend+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Active+Global+Fxd+Inc+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Active+HY+Bd+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Active+Preferred+Share+ETF&pi_universe=PUBLIC_FUND",
"Horizons+AlphaPro+En+IncEng+ETF+Adv&pi_universe=PUBLIC_FUND",
"Horizons+AlphaPro+Enha+Inc+Gold+Adv&pi_universe=PUBLIC_FUND",
"Horizons+AlphaPro+Enhanced+Inc+Gold&pi_universe=PUBLIC_FUND",
"Horizons+Canadian+Black+Swan+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Crude+Oil+Yield+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Crude+Oil+Yield+ETF+Adv+Cl&pi_universe=PUBLIC_FUND",
"Horizons+Enh+Inc+Intl+Eq+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Enh+Inc+Intl+Eq+ETF+Adv&pi_universe=PUBLIC_FUND",
"Horizons+Enhanced+Inc+Engy+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Enhanced+Inc+Fin+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Glo+Curr+Opportunities+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Global+Risk+Parity+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Gold+Yield+ETF&pi_universe=PUBLIC_FUND",
"Horizons+Gold+Yield+ETF+Adv+Cl&pi_universe=PUBLIC_FUND",
"Horizons+HFP&pi_universe=PUBLIC_FUND",
"Horizons+HFP.A&pi_universe=PUBLIC_FUND",
"Horizons+HHF+Advs+Cl&pi_universe=PUBLIC_FUND",
"Horizons+High+Yield+Bond+ETF&pi_universe=PUBLIC_FUND",
"Horizons+High+Yield+Bond+ETF+Adv+Cl&pi_universe=PUBLIC_FUND",
"Horizons+HMF&pi_universe=PUBLIC_FUND",
"Horizons+HMF.A&pi_universe=PUBLIC_FUND",
"Antrim+Balanced+Mortgage+Fd+C+Cl+F&pi_universe=PUBLIC_FUND",
"Antrim+Balanced+Mortgage+Fund+A&pi_universe=PUBLIC_FUND",
"Antrim+Balanced+Mortgage+Fund+B&pi_universe=PUBLIC_FUND",
"Arrow+Global+Growth+Fund+Class+A&pi_universe=PUBLIC_FUND",
"Arrow+Global+Growth+Fund+Class+F&pi_universe=PUBLIC_FUND",
"Curvature+Market+Neutral+Fund&pi_universe=PUBLIC_FUND",
"East+Coast+Invest+Grade+II+Fd+A&pi_universe=PUBLIC_FUND",
"East+Coast+Invest+Grade+II+Fd+F&pi_universe=PUBLIC_FUND",
"East+Coast+Investment+Grade+II+Fd+G&pi_universe=PUBLIC_FUND",
"East+Coast+Investment+Grade+II+Fd+U&pi_universe=PUBLIC_FUND",
"Exemplar+Canadian+Focus+Port+Cl+A&pi_universe=PUBLIC_FUND",
"Exemplar+Canadian+Focus+Port+Cl+F&pi_universe=PUBLIC_FUND",
"Exemplar+Canadian+Focus+Port+Cl+L&pi_universe=PUBLIC_FUND",
"Exemplar+Diversified+Portfolio+A&pi_universe=PUBLIC_FUND",
"Exemplar+Diversified+Portfolio+F&pi_universe=PUBLIC_FUND",
"Exemplar+Diversified+Portfolio+L&pi_universe=PUBLIC_FUND",
"Exemplar+Growth+and+Income+Series+A&pi_universe=PUBLIC_FUND",
"Exemplar+Growth+and+Income+Series+L&pi_universe=PUBLIC_FUND",
"Exemplar+Growth+and+Income+Srs+AN&pi_universe=PUBLIC_FUND",
"Exemplar+Growth+and+Income+Srs+FN&pi_universe=PUBLIC_FUND",
"Exemplar+Growth+and+Income+Srs+I&pi_universe=PUBLIC_FUND",
"Exemplar+Investment+Grade+Series+A&pi_universe=PUBLIC_FUND",
"Exemplar+Investment+Grade+Series+AI&pi_universe=PUBLIC_FUND",
"Exemplar+Investment+Grade+Series+AN&pi_universe=PUBLIC_FUND",
"Exemplar+Investment+Grade+Series+F&pi_universe=PUBLIC_FUND",
"Exemplar+Investment+Grade+Series+FN&pi_universe=PUBLIC_FUND",
"Exemplar+Investment+Grade+Srs+G+USD&pi_universe=PUBLIC_FUND",
"Exemplar+Leaders+Fund+Series+A&pi_universe=PUBLIC_FUND",
"Exemplar+Leaders+Fund+Series+F&pi_universe=PUBLIC_FUND",
"Exemplar+Performance+Series+A&pi_universe=PUBLIC_FUND",
"Exemplar+Performance+Series+F&pi_universe=PUBLIC_FUND",
"Exemplar+Performance+Series+FD&pi_universe=PUBLIC_FUND",
"Exemplar+Performance+Series+L&pi_universe=PUBLIC_FUND",
"Exemplar+Performance+Series+LD&pi_universe=PUBLIC_FUND",
"Exemplar+Tactical+Corp+Bd+Srs+M+USD&pi_universe=PUBLIC_FUND",
"Exemplar+Tactical+Corporate+Bond+A&pi_universe=PUBLIC_FUND",
"Exemplar+Tactical+Corporate+Bond+AI&pi_universe=PUBLIC_FUND",
"Exemplar+Tactical+Corporate+Bond+AN&pi_universe=PUBLIC_FUND",
"Exemplar+Tactical+Corporate+Bond+F&pi_universe=PUBLIC_FUND",
"Exemplar+Tactical+Corporate+Bond+FI&pi_universe=PUBLIC_FUND",
"Exemplar+Tactical+Corporate+Bond+FN&pi_universe=PUBLIC_FUND",
"Exemplar+Tactical+Corporate+Bond+L&pi_universe=PUBLIC_FUND",
"EXP+Investment+Grade+Srs+FI&pi_universe=PUBLIC_FUND",
"Hirsch+Performance+Fund&pi_universe=PUBLIC_FUND",
"Lazard+Global+Credit+II+Class+A&pi_universe=PUBLIC_FUND",
"Lazard+Global+Credit+II+Class+F&pi_universe=PUBLIC_FUND",
"Lazard+Global+Credit+II+Class+G&pi_universe=PUBLIC_FUND",
"Lazard+Global+Credit+II+Class+U&pi_universe=PUBLIC_FUND",
"Northern+Rivers+Cons+Growth+LP&pi_universe=PUBLIC_FUND"]



#alpha pro




workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('text')

row=0
col=0
for fund in fund_list:
    col=0


    url = base_url + fund

    sauce=urllib.request.urlopen(url)

    soup=BeautifulSoup(sauce,'html.parser')


    l=[]

    for name in soup.find_all('title'):
        l.append(str(name.text))

    for result in soup.find_all('font'):
        l.append(str(result.text))




    FUND=l[0]



    index_MER=l.index("Mgmt Expense Ratio (MER):")
    MER=l[index_MER+1] 

    index_FUNDTYPE=l.index("Fund Type:")
    FUNDTYPE=l[index_FUNDTYPE+1]

    index_CURRENT_PRICE=l.index("Current Price:")
    CURRENT_PRICE=l[index_CURRENT_PRICE+1]

    index_FUND_RETURN=l.index("Year-to-Date:")
    FUND_RETURN=l[index_FUND_RETURN+1]

    index_THREE_YEAR_RISK=l.index("3 year risk")
    THREE_YEAR_RISK1=l[index_THREE_YEAR_RISK+1]
    THREE_YEAR_RISK2=l[index_THREE_YEAR_RISK+2]
    THREE_YEAR_RISK3=l[index_THREE_YEAR_RISK+3]

    index_THREE_YEAR_BETA=l.index("3 year beta")
    THREE_YEAR_BETA1=l[index_THREE_YEAR_BETA+1]
    THREE_YEAR_BETA2=l[index_THREE_YEAR_BETA+2]
    THREE_YEAR_BETA3=l[index_THREE_YEAR_BETA+3]


    index_list=[FUND_RETURN,CURRENT_PRICE,MER,THREE_YEAR_RISK1,THREE_YEAR_RISK2,THREE_YEAR_RISK3,
    THREE_YEAR_BETA1,THREE_YEAR_BETA2,THREE_YEAR_BETA3,FUNDTYPE,FUND]
    
    for element in index_list:
        worksheet.write(row, col, element)
        col=col+1


    row=row+1
    

workbook.save('text.xls')



