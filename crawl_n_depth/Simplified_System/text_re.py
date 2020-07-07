import re


text = "Our offices Sydney 5 Blackfriars Street Chippendale NSW 2008 Australia Melbourne Ground Floor 430 Little Collins Street Melbourne VIC 3000 Australia Perth Suite 2, Churchill Court 234 Churchill Avenue Subiaco WA 6008 Australia Canberra Building 5 1 Dairy Rd Fyshwick ACT 2609 Australia 2and2"

addregexau = re.compile(r"(?i)(\\b(PO BOX|post box)[,\s|.\s|,.|\s]*)?(\b(\d+))(\b(?:(?!\s{2,}).){1,60})\b(New South Wales|Victoria|Queensland|Western Australia|South Australia|Tasmania|VIC|NSW|ACT|QLD|NT|SA|TAS|WA).?[,\s|.\s|,.|\s]*(\b\d{4}).?[,\s|.\s|,.|\s]*(\b(Australia|Au))?")
searchau = re.findall(addregexau,text)
# for each in searchau:
#     add_l = []
#     add_r =list(each)
#     for each_r in add_r:
#         if(each_r not in add_l):
#             add_l.append(each_r)
#     # print(add_l)
#     add_f = (" ").join(add_l).strip()
#     print(add_f)
# if (len(searchau)):
#     add_r = (" ").join(list(searchau[0]))
#     add_r = add_r.strip()
#     print(add_r)
# address = ['Unit  41 , 159 Arthur Street, Homebush West, NSW 2140 Australia', '41 /159 Arthur Street Homebush NSW Australia', 'Unit  41 , 159 Arthur Street Homebush West,  NSW 2140 Australia', 'Unit  41 , 159 Arthur Street Homebush West,    NSW 2140 Australia', 'Unit  41 , 159 Arthur Street Homebush West, Sydney, NSW Australia', 'Unit  41 , 159 Arthur Street, Homebush West, Sydney, NSW Australia 2140', 'Unit  41 , 159 Arthur Street Homebush West, NSW 2140 Australia', 'Unit  41 , 159 Arthur Street, Homebush West, NSW 2140']
address = [['Unit 14, 538 Gardeners Road Alexandria NSW 2015 Australia', '14 , 538 Gardeners Road Alexandria NSW, 2015 Australia', '10 , World Trade Centre 611 Flinders Street Melbourne, VIC 3005', 'Unit 14, 538 Gardeners Road Alexandria NSW 2015', '14 , 538 Gardners Road Alexandria, NSW 2015']
,['SUITE 125, 26-32 PIRRAMA ROAD, PYRMONT, NEW SOUTH WALES 2009', '125 , 26-32 Pirrama Road, Pyrmont, New South Wales 2009', 'Suite 125, 26-32 Pirrama Road, Pyrmont, New South Wales 2009', '125 , Jones Bay Wharf 26-32 Pirrama Road Pyrmont, NSW 2009']
,['PO Box 8417 Symonds Street  Auckland New Zealand', '100 New North Rd Eden Terrace, Auckland 1021', '100 New North Rd, Eden Terrace, Auckland 1021']
,['PO Box 814 Chatswood NSW 2057 Australia', '1 , 67 Albert Avenue, Chatswood NSW 2067', '814 , Chatswood NSW 2067', 'PO Box 814 Chatswood NSW  2057']
,['PO Box 4301 , Shortland Street  Auckland 1140', 'PO Box 4301, Shortland Street, Auckland 1140', 'PO Box 4301 , Shortland Street Auckland 1140 New Zealand', 'PO Box 4301, Shortland Street, Auckland 1140 New Zealand']
,['PO Box 393, Kumeu Auckland 0841 New Zealand', 'PO Box 393, Kumeu Auckland 0841']
,['PO Box 327 , Arana Hills QLD  4054', 'PO Box 327 , Arana Hills QLD 4054']
,['PO Box 322 , Yeppoon, Qld 4703 Au', 'PO Box 322 , Yeppoon QLD  4703', 'PO Box 322 , Yeppoon QLD 4703', 'PO Box 322 , Yeppoon, Qld  4703']
,['Level 26/1 Bligh St, Sydney NSW 2000']
,['Level 2, 155 Queen St, Brisbane City QLD 4000', '16 , 215 Adelaide St, Brisbane QLD 4000', 'Level 3, 11-31 York St, Wynyard, NSW 2000', '3 , 11-31 York St, Wynyard, NSW 2000', '28 UltimoRd,Ultimo, NSW 2007', '4 , 155 Queen St, Brisbane City QLD 4000', '155 Waymouth St, Adelaide SA 5000', '7 :30 am åœ°ç‚¹ 89-91 City Rd Southbank, 3006, Victoria Australia', '14 %2F28UltimoRd,Ultimo NSW 2007', 'Level 16, 215 Adelaide St, Brisbane QLD 4000', '4 , 155 Queen St, Brisbane City, QLD 4000', '7 :00 am åœ°ç‚¹ 89-91 City Rd Southbank, 3006, Victoria Australia', '2 , 155 Queen St, Brisbane City QLD 4000', '11 :00 am åœ°ç‚¹ (Level2) 315 Brunswick StreetFortitude Valley QLD 4006']
,['Level 18, 1 Margaret St Sydney NSW 2000 Australia', 'Level 18, 1 Margaret St, Sydney NSW 2000', 'Level 18, 1 Margaret St, Sydney NSW 2000 Australia']
,['Level 1 235 â€“ 239 Commonwealth Street Surry Hills, NSW 2010']
,['9 Tanbark  Circuit Werrington  Downs NSW 2747', '9 Tanbark  Circuit Werrington  Downs NSW 2747 Australia']
,['88 Creek St Brisbane 4000', '427 City Road   South Melbourne VIC 3205']
,['8 Whiteman St Southbank VIC 3006 Australia', '2 , 52 Davidson Terrace Joondalup WA 6027', '4 /303 Burwood Highway Burwood East VIC 3151', '2684 -2690 Gold Coast Hwy Broadbeach Queensland 4218', '8 Whiteman St   Southbank , VIC 3006 Australia', '1 Davey St Hobart Tasmania 7000', '14 Darling Dr Sydney NSW 2000', '14 Darling Drive   Sydney , NSW 2009 Australia', '14 Darling Drive Sydney NSW 2009', '8 Whiteman St   Southbank , VIC 3006', '116 Sussex Street   Sydney , NSW 2000', '8 Whiteman St Southbank ,  VIC 3006 Australia', '1 Convention Centre Place   South Wharf , Victoria 3006', '4 /303-313 Burwood Highway, Burwood East, VIC 3151 Australia', '2684 -2690 Gold Coast Hwy   Broadbeach , Queensland 4218', '14 Darling Drive   Sydney , NSW 2009', '1 Convention Centre Place South Wharf Victoria 3006 Australia', '1 Davey St Hobart ,  Tasmania 7000 Australia', '14 Darling Dr   Sydney , NSW 2000', 'PO Box 740 Joondalup WA 6919', '116 Sussex Street   Sydney , NSW 2000 Australia', '116 Sussex Street Sydney NSW 2000 Australia', '17 Potters Hill Road   San Remo , Victoria 3925 Australia', '8 Whiteman St Southbank VIC 3006', 'PO Box 740 Joondalup WA  6919', '17 Potters Hill Road San Remo Victoria 3925 Australia', '1 Davey St Hobart Tasmania 7000 Australia', '116 Sussex Street Sydney NSW 2000', '2684 -2690 Gold Coast Hwy, Broadbeach, Queensland 4218 Australia', '14 Darling Dr   Sydney , NSW 2000 Australia', '17 Potters Hill Road   San Remo , Victoria 3925', '1 Davey St   Hobart , Tasmania 7000 Australia', '1 Convention Centre Place   South Wharf , Victoria 3006 Australia', '17 Potters Hill Road San Remo Victoria 3925', '1 Convention Centre Place, South Wharf, Victoria 3006', '14 Darling Dr Sydney NSW 2000 Australia', '1 Davey St   Hobart , Tasmania 7000', '116 Sussex Street Sydney ,  NSW 2000 Australia', '2684 -2690 Gold Coast Hwy, Broadbeach, Queensland 4218', '17 Potters Hill Road San Remo ,  Victoria 3925 Australia', '1 Convention Centre Place, South Wharf, Victoria 3006 Australia', '1 Convention Centre Place South Wharf Victoria 3006', '4 /303-313 Burwood Highway, Burwood East, VIC 3151', '2684 -2690 Gold Coast Hwy   Broadbeach , Queensland 4218 Australia', '14 Darling Drive Sydney NSW 2009 Australia', '2684 -2690 Gold Coast Hwy Broadbeach Queensland 4218 Australia']
,['8 Dawson Street South Ballarat Central VIC 3350']
,['8 Brookfield Place 125 St Georges Terrace PERTH WA 6000 Australia', '8 , Brookfield Place, 125 St Georges Terrace, Perth WA 6000', '8 Brookfield Place 125 St Georges Terrace PERTH WA 6000']
,['8 100 Creek Street BRISBANE QLD 4000', '10 , 5 Hunter Street, Sydney NSW 2000', '21 October    BDO Centre 420 King William Street ADELAIDE SA 5000', '10 5 Hunter Street SYDNEY NSW 2000', '4 :45pm   BDO Centre 420 King William Street ADELAIDE SA 5000', '20 August    Charles Darwin University Campus & Room TBC NT 0800', '8 Victoria Avenue PERTH WA 6000', '5 :00pm    BDO Centre 420 King William Street ADELAIDE SA 5000', '1594 , Sydney, NSW 2001', '7 500 Collins Street MELBOURNE VIC 3000', '4 :45pm    Charles Darwin University Campus & Room TBC NT 0800', '4 :45pm    BDO Centre 420 King William Street ADELAIDE SA 5000']
,['8 , 410 Burwood Highway, Wantirna South, Victoria 3152']
,['79 St. Georges Bay Road Parnell, Auckland New Zealand', '79 St Georges Bay Rd  Parnell Auckland 1052', '79 St Georges Bay Rd Parnell Auckland 1052', '79 St Georges Bay Rd, Parnell, Auckland 1052', '79 St Georges Bay Rd Parnell, Auckland 1052']
,['79 St Georges Bay Rd Parnell Auckland 1052', '3 Market Lane Wellington 6011', '3 Market Lane, Wellington 6011 New Zealand', '3 Market Lane, Wellington 6011']
,['76 I donâ€™t know  4355    77   M.E.O.  3879    78   BOI BOI WEST COAST 3853', '490 Northbourne Ave, Dickson ACT 2602', '9499 27   Michael FALLETI  9454    28   BOI BOI WEST COAST 9446', '1711 Canberra ACT Australia 2601']
,['74 Doncaster Road Balwyn North, Melbourne, Victoria Australia']
,['71 Silverdale Rd, Eaglemont, Victoria Australia 3084', '71 Silverdale Rd Eaglemont, Victoria Australia']
,['69 Gracefield Road Lower Hutt 5010', '69 Gracefield Road Lower Hutt 5010 New Zealand']
,['655 Parramatta Road Leichardt NSW 2040 Australia', '655 Parramatta Road Leichhardt, NSW 2040 Australia', 'PO Box 250 , Glebe NSW  2037', '655 Parramatta Road Leichhardt NSW 2040', '655 Parramatta Road  Leichardt NSW 2040', '655 Parramatta Road  Leichardt NSW 2040 Australia', '655 Parramatta Road Leichhardt, NSW 2040', 'PO Box 250 , Glebe NSW 2037 Australia']
,['6408 216th Street SW. Mountlake Terrace, WA 9804']
,['61 3 9910 4737 53 Park St South Melbourne Victoria Australia']
,['606 /343 Little Collins Street Melbourne,  Vic 3000 Australia', '606 /343 Little Collins Street Melbourne, Vic 3000 Australia', '606 /343 Little Collins Street Melbourne, Vic 3000']
,['6 , 22 William St Melbourne, 3000 Australia', '6 , 22 William Street  MELBOURNE VIC 3000', '6 , 22 William St Melbourne 3000']
,['6 , 11-31 York Street, Sydney NSW 2000', '6 , 11-31 York Street Sydney NSW 2000 Australia', '6 , 11-31 York Street, Sydney NSW 2000 Australia']
,['586 , Little Collins St Melbourne Victoria Australia', '586 , Little Collins St , Melbourne Victoria Australia 3000']
,['506 Sydney NSW 2001']
,['501 , 280 Pitt Street Sydney 2000']
,['501 , 19a Boundary Street, Darlinghurst, NSW 2010']
,['5 /13 Evans Street, Maroochydore, Queensland Australia 4558', '1300 795 503  Schoolzine Pty Ltd 48 School Road Maroochydore, QLD Australia 4558', '66 2106 4140 Schoolzine Pty Ltd 48 School Road Maroochydore, QLD Australia 4558', '48 School Road Maroochydore, QLD Australia', '5 /13 Evans Street Maroochydore, Queensland Australia']
,['5 , 1 Goldner Circuit, Melba, ACT 2615']
,['47 , 50 St Georges Terrace Perth, WA 6000 Australia', '47 , 50 St Georges Tce, Perth Western Australia 6000', '6 , 191 St Georges Tce, Perth Western Australia 6000', '47 , 50 St Georges Terrace Perth, WA 6000']
,['448 Botany Rd, Beaconsfield NSW 2015', '26 Albert Coates Ln, Melbourne VIC 3000', '14 Underwood Avenue  Botany, NSW 2019 AUSTRALIA', '36 Morley Avenue Rosebery NSW 2018', 'Level 2,  Westfield Newmarket, Auckland 1023', '14 Underwood Avenue Botany NSW 2019 Australia', '7 /65 James\xa0St, Fortitude Valley QLD 4006', '28 Jonson\xa0St, Byron Bay NSW 2481', '14 Underwood Avenue Botany NSW 2019', '2 /8-10 Station St, Bangalow NSW 2479', '14 Underwood Avenue Botany, NSW 2019 AUSTRALIA', '79 - 81 Pittwater Rd, Manly NSW 2095', '221 Bondi Rd, Bondi NSW 2026', '36 Morley Avenue Rosebery NSW 2018 Australia', '14 Underwood Avenue  Botany, NSW 2019', '243 Brunswick St, Fitzroy VIC 3065', 'Level 2,  Westfield Newmarket, Auckland 1023 New Zealand', '262 Oxford St, Paddington NSW 2021', '1062 High St,\xa0Armadale VIC 3143']
,['430 Little Collins Street Melbourne VIC 3000', '430 Little Collins Street Melbourne VIC 3000 Australia', '5 1 Dairy Rd Fyshwick ACT 2609 Australia', '2 , Churchill Court 234 Churchill Avenue Subiaco WA 6008', '883 974.  Our offices Sydney 5 Blackfriars Street Chippendale NSW 2008', '5 1 Dairy Rd Fyshwick ACT 2609', '5 Blackfriars Street Chippendale NSW 2008', '2 , Churchill Court 234 Churchill Avenue Subiaco WA 6008 Australia', '883 974.  Our offices Sydney 5 Blackfriars Street Chippendale NSW 2008 Australia', '5 Blackfriars Street Chippendale NSW 2008 Australia', '5 Blackfriars StreetChippendale, NSW 2008', '5 Blackfriars Street","addressLine2":"Chippendale, NSW 2008', '234 Churchill Avenue Subiaco WA 6008 Australia']
,['43 TherryStreet,Melbourne VIC 3000', '913 /43 Therry Street Melbourne VIC 3000', '913 /43 Therry Street Melbourne CBD 3000 Victoria Australia', '913 /43 Therry Street Melbourne VIC. 3000 Australia', '913 /43 Therry Street Melbourne VIC 3000 Australia']
,['41 , 159 Arthur Street Homebush West, NSW 2140 Australia', '41 , 159 Arthur Street Homebush West,    NSW 2140 Australia', '41 , 159 Arthur Street, Homebush West, NSW 2140 Australia', '41 , 159 Arthur Street, Homebush West, NSW 2140', '41 , 159 Arthur Street, Homebush West, Sydney, NSW Australia 2140', '41 , 159 Arthur Street Homebush West,  NSW 2140 Australia', '41 /159 Arthur Street Homebush NSW Australia', '41 , 159 Arthur Street Homebush West, Sydney, NSW Australia']
,['4 Sibley Street, North Lakes, QLD 4509', '4 Sibley St NORTH LAKES Qld 4509', '4 Sibley St, North Lakes Qld 4509', '528 Kingsford-Smith Drive Hamilton Qld 4007', '4 Sibley St, NORTH LAKES Qld 4509', '528 Kingsford-Smith Drive, Hamilton, QLD 4007', 'PO Box 2167 REDCLIFFE NORTH Qld 4020', 'PO Box 2167 REDCLIFFE NORTH Qld  4020']
,['4 Eastside Business Park 15 Accent Drive East Tamaki Auckland 2013', '4 Eastside Business Park 15 Accent Dve East Tamaki Auckland 2013']
,['4 /64-66 Castlereagh St. Liverpool, NSW Australia 2170', '4 /64-66 Castlereagh St Liverpool, NSW, 2170 Australia', '4 /64-66 Castlereagh St Liverpool, NSW Australia', '4 /64-66 Castlereagh St. Liverpool, NSW 2170 Australia', '4 /64-66 Castlereagh St. Liverpool, NSW 2170']
,['4 /54 Marcus Clarke Street  Canberra ACT 2601', '1 , 140 St Georges Terrace,  Perth , WA 6000', '1 , 33-35 Ainslie Place, Canberra, ACT 2601', '1 , 140 St Georges Terrace Perth WA 6000', '19 Young Street  Adelaide SA 5000', '11 , 32 Walker street, North Sydney, NSW 2060', '11 ,  32 Walker Street North Sydney NSW 2060', '11 , 32 Walker Street North Sydney NSW 2060', '12 , 379 Collins Street Melbourne VIC 3000', '12 , 379 Collins Street, Melbourne, VIC 3000', '19 Young Street,  Adelaide , SA 5000', '1 /140 St Georges Terrace  Perth WA 6000', '4 , 54 Marcus Clarke Street,  Canberra , ACT 2601', '12 379 Collins Street Melbourne VIC 3000', '4 , 54 Marcus Clarke Street Canberra ACT 2601', '12 , 379 Collins Street,  Melbourne , VIC 3000', '6 , 371 Queen Street Brisbane QLD 4000', '11 /32 Walker Street  North Sydney NSW 2060', '19 Young Street, Adelaide, SA 5000', '19 Young Street Adelaide SA 5000', '6 , 371 Queen Street,  Brisbane , QLD 4000', '1 , 140 St Georges Terrace, Perth, WA 6000', '12 /379 Collins Street  Melbourne VIC 3000', '11 , 32 Walker Street,  North Sydney , NSW 2060', '6 , 371 Queens Street, Brisbane, QLD 4000', '6 /371 Queen Street  Brisbane QLD 4000']
,['4 /303-313 Burwood Highway Burwood East VIC 3151', '4 /303-313 Burwood Highway, Burwood East, VIC 3151 Australia', '2 , 52 Davidson Terrace Joondalup WA 6027', '4 /303-313 Burwood Highway, Burwood East, VIC 3151']
,['4 , 11 Finchley Street Milton, QLD 4064', '4 , 11 Finchley Street Milton, QLD 4064 Australia', '4 , 11 Finchley Street Milton, QLD, 4064 Australia']
,['3095 KEW VIC 3101']
,['308 & 309, 2-8 Brookhollow Avenue,  Baulkham Hills, NSW 2153', '308 & 309 2-8 Brookhollow Avenue, Baulkham Hills, NSW 2153']
,['30 Centre Rd Scoresby VIC 3179', '004 245 943 of 707 Collins Street Melbourne, Victoria Australia', '40 004 245 943 of 707 Collins Street, Melbourne, Victoria Australia 3008', '11 New South Wales 2017', '707 Collins Street Melbourne VIC 3008', '707 Collins Street, Melbourne, Victoria Australia 3008', '707 Collins Street Melbourne, Victoria Australia']
,['30 9 Castlereagh Street Sydney NSW 2000  GPO Box 1462 Sydney NSW 2001']
,['3 20 Bond Street Sydney, NSW 2000 Australia', '3 20 Bond Street Sydney, NSW 2000']
,['3 , F 25 Exchange Pl, Barangaroo NSW 2000']
,['3 , 49 Malop St, Geelong, VIC 3220 AUSTRALIA', 'PO BOX 4033 GEELONG VIC 3220', '3 , 49 Malop St Geelong, VIC 3220 AUSTRALIA', '3 , 49 Malop St, Geelong, VIC 3220', 'Po Box 4033 GEELONG VIC AUSTRALIA 3220', 'PO BOX 4033 GEELONG VIC  3220']
,['3 , 41-43 Stewart Street Melbourne 3121', '3 , 41-43 Stewart Street Melbourne Victoria 3121 Australia', '1 , 41-43 Stewart Street, Richmond Victoria Australia 3121', '1 , 41-43 Stewart Street Richmond, VIC 3121 Australia', '1 , 41-43 Stewart Street Richmond, VIC, 3121 Australia', '3 , 41-43 Stewart Street Melbourne, 3121 Australia', '1 , 41-43 Stewart Street Richmond, VIC 3121', '1 , 41-43 Stewart Street Richmond Victoria Australia', '3 , 41-43 Stewart Street Melbourne Victoria 3121']
,['28 , 161 Castlereagh Street Sydney NSW 2000 Australia', '2012 iAward for eLearning â€“ Deloitte Leadership Academy SA', '5 , 126 Phillip Street Sydney NSW 2000 Australia', '3 , Wentworth Park Grandstand, Wattle Street, Glebe NSW 2037 Australia', '9 , 4 Williamson Avenue Grey Lynn, Auckland 1021', '3 , Wentworth Park Grandstand, Wattle Street, Glebe NSW 2037', '5 , 126 Phillip Street Sydney NSW 2000', '9 , 4 Williamson Avenue Grey Lynn, Auckland 1021 New Zealand', '28 , 161 Castlereagh Street Sydney NSW 2000', '3 , Wentworth Park Grandstand  Wattle Street  Glebe NSW 2037', '9 , 4 Williamson Avenue  Grey Lynn, Auckland 1021 New Zealand', '2011 iAward winner for eLearning Excellence NSW', '3 , Wentworth Park Grandstand  Wattle Street  Glebe NSW 2037 Australia', '9 , 4 Williamson Avenue  Grey Lynn, Auckland 1021']
,['255 Wilson Street,  Everleigh, NSW 2015']
,['25 Franklin Street   Adelaide , SA 5000', '12 Gipps St, Collingwood   Melbourne , VIC 3066 Australia', '2 , North Tower 10 Browning St   Brisbane , QLD 4101 Australia', '1 , 507 Murray Street Perth   Perth , WA 6000 Australia', '1 , 507 Murray Street, Perth   Perth , WA 6000 Australia', '51 Allara Street   Canberra , ACT 2601', 'Suite 600   Seattle , WA 9812', '51 Allara Street Canberra, ACT 2601 Australia', '1 , 507 Murray Street, Perth   Perth , WA 6000', '25 Franklin Street   Adelaide , SA 5000 Australia', '3 , 142-146 Elizabeth St   Hobart , TAS 7000', '1 , 100 Tory Street Te Aro   Wellington , 6011 New Zealand', '1 , 100 Tory Street, Te Aro Wellington 6011', 'PO Box 3141 South Brisbane QLD 4101', '1 , 100 Tory Street Te Aro Wellington 6011', '10 Browning St Brisbane , QLD 4101 Australia', '12 Gipps St, Collingwood   Melbourne , VIC 3066', '51 Allara Street Canberra, ACT 2601', '1 , 100 Tory Street, Te Aro Wellington 6011 New Zealand', '2 , North Tower 10 Browning St   Brisbane , QLD 4101', '3 , 142-146 Elizabeth St Hobart , TAS 7000 Australia', '51 Allara Street   Canberra , ACT 2601 Australia', '25 Franklin Street Adelaide , SA 5000 Australia', '3 , 142-146 Elizabeth St   Hobart , TAS 7000 Australia', '51 Allara Street Canberra , ACT 2601 Australia', 'PO Box 3141 South Brisbane QLD  4101']
,['25 Chapel Street, St Kilda VIC 3182', '25 Chapel Street, St Kilda VIC 3182 Australia']
,['25 , 88 Phillip St, Sydney NSW 2000', '25 , 88 Phillip St, Sydney NSW 2000 Australia', '25 , 88 Phillip St Sydney NSW 2000 Australia', '1100 5th Ave, Seattle, WA 9810']
,['243 Hay Street, Subiaco WA 6008 Australia', '243 Hay Street Subiaco WA 6008 Australia', '243 Hay Street Subiaco WA 6008', '243 Hay Street, Subiaco WA 6008']
,['239 , Innovation Campus, Squires Way, North Wollongong NSW 2500', '3 /239 Innovation Way North Wollongong NSW 2500', '239 , Innovation Campus, Squires Way, North Wollongong NSW 2500 Australia']
,['231 , Chapel St Prahran, VIC Australia', '231 Chapel St, Prahran, Victoria Australia 3181', '2016 . So it wa', '231 Chapel St Prahran, Victoria Australia']
,['208 Glenmore Road, Paddington NSW 2021']
,['2013 /12/Mathletics-Hillard-State- QLD', '18 , 124 Walker Street, North Sydney, NSW 2060']
,['2010 Synergetic employs its first interstate staff member in WA 2013', '4 /303-313 Burwood Highway, Burwood East, VIC 3151 Australia', '4 /303-313 Burwood Hwy, Burwood East, Victoria 3151', 'Level 4, 655 Pacific Highway St Leonards, NSW 2065', '2 , 52 Davidson Terrace, Joondalup, WA 6027 Australia', '4 , 303 Burwood Highway Burwood East, Vic 3151', '2 , 52 Davidson Terrace, Joondalup, WA 6027', '4 /303-313 Burwood Hwy, Burwood East, Victoria 3151 Australia', '4 /303-313 Burwood Highway, Burwood East, VIC 3151', 'Level 4, 655 Pacific Highway St Leonards, NSW 2065 Australia', '4 , 655 Pacific Highway St Leonards, NSW 2065 Australia']
,['2001 , ASIC Act', 'PO Box 243 Prahran, Victoria 3181', 'PO Box 243 Prahran, Victoria  3181']
,['200 Pulteney St Adelaide, South Australia 5000 Australia', '200 Pulteney St, Adelaide, South Australia 5000', '200 Pulteney St, Adelaide, South Australia 5000 Australia']
,['2 Wentworth Park Grandstand Wattle Street Ultimo NSW 2007', 'Suite 405, Seattle, WA 9810', '49 Phillip Avenue Watson ACT 2602', '18 -38 Siddeley Street Melbourne VIC 3005', '3 32 Grenfell Street Adelaide SA 5000']
,['2 , 83-97 Kippax Street Surry Hills, NSW 2010']
,['2 , 186 Willis Street, Te Aro, Wellington Wellington 6011 New Zealand', '2 , 186 Willis Street, Te Aro, Wellington Wellington 6011', '28 , 100 Willis Street Wellington 6011', '26 National Street Leichhardt 2040 Australia', '28 , 100 Willis Street, Wellington 6011', '28 , 100 Willis Street Wellington 6011 New Zealand', '2 , 186 Willis Street Te Aro Wellington 6011 New Zealand', '2 , 186 Willis Street Te Aro, Wellington Wellington 6011', '2 , 186 Willis Street Te Aro Wellington 6011', '28 , 100 Willis Street, Wellington 6011 New Zealand']
,['2 , 11 York Street Wynyard, Sydney 2000', '30 Hickson Road, Millers Point NSW 2000', '7 , 7-9 Mallett Road, Tullamarine VIC 3043', '10 u002F110 Caroline Street, South Yarra. VIC 3141', '500 ","company_address":"800 Toorak Rd, Hawthorn East VIC 3123', '13 , 50 Carrington Street, Sydney NSW 2000'],['185 Malop Street, Geelong VIC 3220', '3 /50 York St, Sydney NSW 2000', '9 Pakington St St Kilda VIC 3182', '31 Birrell St Bondi Junction NSW 2022', '3220 Perth Office  45 St Georges Terrace, Perth 6000', '138 Bondi Road, Bondi NSW 2026', '3182 Sydney Office  135-153 New South Head Road, Edgecliff, NSW 2027', '185 Malop Street Geelong VIC 3220', '2 Maxwell Ave Milperra NSW 2214', '1 , 3 Wellington Street St Kilda VIC 3182', '60 Playne Street Frankston VIC 3199', '1 /3 Wellington St, St Kilda VIC 3182', '8 River Rd Ermington NSW 2115'],['182 -222 Lake Rd, Wallsend NSW 2287', '2302 Maitland Campus - 416A High St, Maitland NSW 2320', '461 King St Newcastle West NSW 2302'],['17 144 Edward Street Brisbane, Queensland 4000 Australia', '17 600 Bourke Street Melbourne, Victoria 3000 Australia', 'Suite 1.02, Level 1, 17 Moore Street, Canberra ACT 2601 Australia', 'Level 17, 600 Bourke St, Melbourne VIC 3000', '25 , 8-12 Chifley Square, Sydney NSW 2000 Australia', '25 , 8-12 Chifley Square, Sydney NSW 2000', 'Level 17 144 Edward Street, Brisbane, Queensland 4000', 'Level 10 11 Britomart Place Auckland 1010 New Zealand', 'Level 17, 144 Edward Street, Brisbane QLD 4000 Australia', 'Level 1, 17 Moore Street Canberra ACT, 2601 Australia', 'Level 17, 600 Bourke St, Melbourne VIC 3000 Australia', 'Level 17 600 Bourke Street, Melbourne, Victoria 3000 Australia', 'Level 17 600 Bourke Street, Melbourne, Victoria 3000', 'Level 17, 144 Edward Street, Brisbane QLD 4000', 'Level 10 11 Britomart Place Auckland 1010', '17 , 144 Edward Street Brisbane QLD, 4000 Australia', 'Level 17 144 Edward Street, Brisbane, Queensland 4000 Australia', '17 , 600 Bourke St Melbourne VIC, 3000 Australia', 'Suite 1.02, Level 1, 17 Moore Street, Canberra ACT 2601', '25 8-12 Chifley Square, Sydney, New South Wales 2000 Australia', '25 8-12 Chifley Square, Sydney, New South Wales 2000'],['15 22-36 Mountain Street Ultimo, NSW 2007', '16 22-36 Mountain Street, Ultimo, NSW 2007 Australia', '16 22-36 Mountain Street Ultimo, NSW, 2007 Australia', '15 22-36 Mountain Street Ultimo, NSW, 2007 Australia', '16 22-36 Mountain Street, Ultimo, NSW 2007', '15 22-36 Mountain Street Ultimo, NSW 2007 Australia'],['1300 565 696  3/23 Main St  VARSITY LAKES QUEENSLAND 4227 AUSTRALIA', 'Level 13, 333 George Street  SYDNEY, NEW SOUTH WALES 2000 AUSTRALIA', '3 /23 Main St VARSITY LAKES QUEENSLAND 4227', '3 /23 Main St VARSITY LAKES QUEENSLAND 4227 AUSTRALIA', 'Level 13, 333 George Street SYDNEY, NEW SOUTH WALES 2000 AUSTRALIA', 'PO Box 1001 ROBINA QLD 4226', 'Level 13, 333 George Street  SYDNEY, NEW SOUTH WALES 2000', 'PO Box 1001 ROBINA QLD  4226', '1300 565 696  3/23 Main St VARSITY LAKES  QUEENSLAND 4227 AUSTRALIA', '1300 565 696  3/23 Main St  VARSITY LAKES QUEENSLAND 4227'],['115 Victoria Street Melbourne Vic 3000', '115 Victoria Street Melbourne Vic 3000 Australia'],['11 Camford Street MILTON, QLD 4064', '11 Camford Street, Milton, QLD 4064', 'PO Box 1351, Toowong, QLD 4066'],['11 380 St Kilda Rd Victoria 3004 Australia', '1 Kent Street Millers Point NSW 2000 Australia', '1 Kent Street Millers Point NSW 2000', '11 380 St Kilda Rd Victoria 3004'],['11 , 484 St Kilda Road Melbourne VIC 3000 Australia', '11 , 484 St Kilda Road, Melbourne VIC 3000', '11 , 484 St Kilda Road, Melbourne VIC 3000 Australia'],['103 /109 Alexander Street CROWS NEST SYDNEY, NSW AUSTRALIA', '103 /109 Alexander Street CROWS NEST NSW 2065 Australia', '103 /109 Alexander Street CROWS NEST NSW 2065', '103 -4 109 Alexander Street CROWS NEST Sydney NSW AUSTRALIA', '103 -4 109 Alexander Street  CROWS NEST Sydney NSW AUSTRALIA 2065', '103 /109 Alexander Street CROWS NEST SYDNEY, NSW AUSTRALIA 2065'],['1 Queens Road","addressLine2":"Melbourne, VIC 3004'],['1 .02 147 Wharf Street Spring Hill QLD 4000', '53 Dryburgh Street, West Melbourne, VIC 3003', '3 , Lower Ground 301A Castlereagh Street Sydney NSW 2000', '28 Astor Terrace, Spring Hill QLD 4000', '53 Dryburgh Street West Melbourne VIC 3003', '53 Dryburgh Street, West Melbourne VIC 3003', '1 .02, 147 Wharf Street, Spring Hill QLD 4000', '3 , Lower Ground, 301A Castlereagh Street, Sydney NSW 2000'],['1 , Room 112, 838 Collins Street, Docklands VIC 3008', '5218 , Sydney NSW 2001', 'Suite 3.01, 850 Collins Street, Docklands, VIC 3008', '3 .01 850 Collins Street Docklands Victoria 3008', '4 93 York Street Launceston Tasmania 7250'],['1 , 77 King St   Perth WA 6000'],['1 , 6 Colin Jamieson Drive Welshpool, WA 6106', '15 , Perry Park Estate 33 Maddox Street Alexandria, NSW 2015', '14 , 67 Depot Street Banyo, QLD 4014', '9 Commercial Street Marleston, SA 5033', '352 Ferntree Gully Road Notting Hill, VIC 3168'],['1 , 144 George Street Fitzroy, Victoria, 3065 Australia', '1 , 144 George St Fitzroy, Victoria 3065', "20 /36 O'Riordan Street Alexandria, New South Wales 2015", '20 /36 Oâ€™Riordan St Alexandria, NSW 2015', '1 , 144 George Street, Fitzroy, Victoria 3065', '1 , 144 George Street, Fitzroy, Victoria 3065 Australia'],['1 , 122-126 Old Pittwater Road Brookvale, NSW 2100', '1 , 122-126 Old Pittwater Road Brookvale, NSW 2100 Australia', 'PO Box 6614 , Frenchs Forest, NSW 2086', 'PO Box 6614 , Frenchs Forest, NSW  2086']

]
def getting_uniques(ad_list):
    mapping_list = []
    fixed_ad_list = []
    fixed_orginal_list = []
    fixed = []
    for y in ad_list:
        yt=y.replace(","," ")
        fixed.append((" ").join(yt.split()))
        mapping_list.append([y,(" ").join(yt.split())])

    fixed = list(set(fixed))
    for i in fixed:
        is_unique = True
        for j in fixed:
            if(i==j):continue
            if(i in j):
                is_unique=False
                break
        if(is_unique):
            fixed_ad_list.append(i)
    for each_i in fixed_ad_list:
        for each_map in mapping_list:
            if(each_map[1]==each_i):
                # print(each_map[0])
                fixed_orginal_list.append(each_map[0])
                break
    # print(ad_list)
    # print(fixed)
    # print(fixed_ad_list)
    # print(fixed_orginal_list)
    return fixed_orginal_list
# getting_uniques(address)
for each_a in address:
    print(each_a)
    print(getting_uniques(each_a))
    print("****")