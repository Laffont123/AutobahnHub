# Proposition d’audit d’identité réelle et de redondance (non destructif)

**Aucune suppression, modification ou réattribution n’a été effectuée.** Ce rapport compare l’identité déclarée avec la photographie réellement affichée. Les paramètres d’URL sont normalisés afin que `sig=` ne transforme pas une même photographie en fausses photos distinctes.

## Résumé

| Indicateur | Résultat |
|---|---:|
| Annonces auditées | **362** |
| Sources photographiques normalisées | **10** |
| Annonces avec conflit catégorie ↔ photo | **231** |
| Groupes même photo + même marque/modèle déclaré | **75** |
| Candidats redondants forts (hors représentant de chaque groupe) | **171** |

## Interprétation

Une différence de prix, de kilométrage, de version ou d’identifiant n’est pas considérée comme une preuve suffisante d’un véhicule physique différent lorsque la même photo principale normalisée est réutilisée pour le même modèle déclaré. À l’inverse, un même modèle n’est pas supprimé uniquement parce qu’il apparaît plusieurs fois : il est conservé lorsque la présentation fournit des éléments réellement distincts.

## Groupes même photo + même identité déclarée

| Image normalisée | Marque | Modèle | IDs du groupe |
|---|---|---|---|
| `photo-1618843479313-40f8afb4b4d8` | Claas | 8R 410 | 60171, 60231 |
| `photo-1618843479313-40f8afb4b4d8` | Claas | 933 Vario ProfiPlus | 60151, 60211 |
| `photo-1502877338535-766e1452684a` | Claas | Axion 870 | 60049, 60069, 60089, 60109, 60129 |
| `photo-1555215695-3004980ad54e` | Claas | Axion 870 | 60010, 60030 |
| `photo-1502877338535-766e1452684a` | John Deere | 8R 410 | 60059, 60079, 60099, 60119, 60139 |
| `photo-1618843479313-40f8afb4b4d8` | John Deere | Axion 870 | 60161, 60221 |
| `photo-1563720223185-11003d516935` | MAN | Lion's Coach R08 | 60077, 60137 |
| `photo-1502877338535-766e1452684a` | MAN | Lion's Coach R08 | 60149, 60179, 60209 |
| `photo-1563720223185-11003d516935` | MAN | Travego 15 SHD | 60047, 60107 |
| `photo-1563720223185-11003d516935` | Mercedes-Benz | Lion's Coach R08 | 60057, 60117 |
| `photo-1502877338535-766e1452684a` | Mercedes-Benz | Travego 15 SHD | 60159, 60189, 60219 |
| `photo-1502877338535-766e1452684a` | Mercedes-Benz / Setra | Iveco Crossway | 150009, 150019, 150029 |
| `photo-1583121274602-3e2820c69888` | Mercedes-Benz / Setra | MAN Lion's | 150005, 150015, 150025, 150035 |
| `photo-1603584173870-7f23fdae1b7a` | Mercedes-Benz / Setra | Mercedes-Benz Citaro | 150002, 150012, 150022, 150032 |
| `photo-1541899481282-d53bffe3c35d` | Mercedes-Benz / Setra | Mercedes-Benz Intouro | 150003, 150013, 150023, 150033 |
| `photo-1618843479313-40f8afb4b4d8` | Mercedes-Benz / Setra | Mercedes-Benz Tourismo | 150001, 150011, 150021, 150031 |
| `photo-1525609004556-c46c7d6cf023` | Mercedes-Benz / Setra | Neoplan Tourliner | 150006, 150016, 150026, 150036 |
| `photo-1563720223185-11003d516935` | Mercedes-Benz / Setra | Scania Interlink | 150007, 150017, 150027, 150037 |
| `photo-1503376780353-7e6692767b70` | Mercedes-Benz / Setra | Setra S | 150004, 150014, 150024, 150034 |
| `photo-1555215695-3004980ad54e` | Mercedes-Benz / Setra | VDD Futura | 150010, 150020, 150030 |
| `photo-1542282088-72c9c27ed0cd` | Mercedes-Benz / Setra | Volvo 9700 | 150008, 150018, 150028, 150038 |
| `photo-1502877338535-766e1452684a` | Setra | Tourismo M | 60169, 60199, 60229 |
| `photo-1563720223185-11003d516935` | Setra | Travego 15 SHD | 60067, 60127 |
| `photo-1618843479313-40f8afb4b4d8` | BMW | Série 3 | 60001, 60011, 60021, 60031 |
| `photo-1555215695-3004980ad54e` | BMW | Série 3 | 60040, 60050, 60060, 60070, 60080, 60090, 60100, 60110, 60120, 60130, 60140 |
| `photo-1603584173870-7f23fdae1b7a` | BMW | Série 3 | 30002, 60142, 60152, 60162, 60172, 60182, 60192, 60202, 60212, 60222, 60232 |
| `photo-1618843479313-40f8afb4b4d8` | Mercedes-Benz | Classe C | 1, 30001 |
| `photo-1618843479313-40f8afb4b4d8` | Volkswagen | Golf VIII R | 90001, 90011 |
| `photo-1583121274602-3e2820c69888` | Volkswagen | Golf VIII R | 90005, 120005 |
| `photo-1541899481282-d53bffe3c35d` | Volkswagen | Transporter T6.1 | 3, 60043, 60073, 60103, 60133 |
| `photo-1563720223185-11003d516935` | BMW | 2000CS | 60167, 60227 |
| `photo-1563720223185-11003d516935` | BMW | 300SL Gullwing | 60147, 60207 |
| `photo-1583121274602-3e2820c69888` | BMW | 911 Turbo 3.3 | 60045, 60065, 60085, 60105, 60125 |
| `photo-1525609004556-c46c7d6cf023` | BMW | 911 Turbo 3.3 | 60006, 60026 |
| `photo-1583121274602-3e2820c69888` | Mercedes-Benz | 911 Turbo 3.3 | 60055, 60075, 60095, 60115, 60135 |
| `photo-1525609004556-c46c7d6cf023` | Mercedes-Benz | 911 Turbo 3.3 | 60016, 60036 |
| `photo-1563720223185-11003d516935` | Mercedes-Benz | 911 Turbo 3.3 | 60157, 60217 |
| `photo-1603584173870-7f23fdae1b7a` | Audi | M850i | 60062, 60122 |
| `photo-1603584173870-7f23fdae1b7a` | Audi | RS5 Coupé | 60042, 60102 |
| `photo-1503376780353-7e6692767b70` | Audi | RS5 Coupé | 60144, 60164, 60184, 60204, 60224 |
| `photo-1503376780353-7e6692767b70` | BMW | M4 Competition | 60154, 60174, 60194, 60214, 60234 |
| `photo-1603584173870-7f23fdae1b7a` | BMW | M4 Competition | 60052, 60112 |
| `photo-1603584173870-7f23fdae1b7a` | BMW | RS5 Coupé | 60072, 60132 |
| `photo-1525609004556-c46c7d6cf023` | Audi | Taycan 4S | 60156, 60176, 60196, 60216, 60236 |
| `photo-1503376780353-7e6692767b70` | Audi | Taycan 4S | 60054, 60084, 60114 |
| `photo-1503376780353-7e6692767b70` | Audi | i4 M50 | 60064, 60094, 60124 |
| `photo-1525609004556-c46c7d6cf023` | Audi | i4 M50 | 60146, 60166, 60186, 60206, 60226 |
| `photo-1583121274602-3e2820c69888` | Audi | iX xDrive40 | 60005, 60035 |
| `photo-1503376780353-7e6692767b70` | Audi | iX xDrive40 | 60044, 60074, 60104, 60134 |
| `photo-1542282088-72c9c27ed0cd` | Ford | Crafter Transfer | 60068, 60128 |
| `photo-1555215695-3004980ad54e` | Ford | Crafter Transfer | 60170, 60200, 60230 |
| `photo-1542282088-72c9c27ed0cd` | Mercedes-Benz | Crafter Transfer | 60048, 60108 |
| `photo-1555215695-3004980ad54e` | Mercedes-Benz | Crafter Transfer | 60150, 60180, 60210 |
| `photo-1542282088-72c9c27ed0cd` | Mercedes-Benz | V-Class VIP | 60078, 60138 |
| `photo-1555215695-3004980ad54e` | Volkswagen | Crafter Transfer | 60160, 60190, 60220 |
| `photo-1542282088-72c9c27ed0cd` | Volkswagen | V-Class VIP | 60058, 60118 |
| `photo-1541899481282-d53bffe3c35d` | Audi | GLE 350d | 60153, 60173, 60193, 60213, 60233 |
| `photo-1618843479313-40f8afb4b4d8` | Audi | GLE 350d | 60071, 60111 |
| `photo-1618843479313-40f8afb4b4d8` | Audi | Q7 50 TDI | 60041, 60081, 60121 |
| `photo-1541899481282-d53bffe3c35d` | Audi | Q7 50 TDI | 60143, 60163, 60183, 60203, 60223 |
| `photo-1618843479313-40f8afb4b4d8` | Audi | Touareg V6 | 60051, 60091, 60131 |
| `photo-1618843479313-40f8afb4b4d8` | Audi | X3 xDrive20d | 60061, 60101, 60141 |
| `photo-1542282088-72c9c27ed0cd` | MAN | Arocs 3342 | 60158, 60218 |
| `photo-1525609004556-c46c7d6cf023` | MAN | TGX 18.510 | 60056, 60076, 60096, 60116, 60136 |
| `photo-1563720223185-11003d516935` | MAN | TGX 18.510 | 60017, 60037 |
| `photo-1542282088-72c9c27ed0cd` | Volvo | Actros 1845 LS | 60168, 60228 |
| `photo-1563720223185-11003d516935` | Volvo | Antos 1832 | 60007, 60027 |
| `photo-1525609004556-c46c7d6cf023` | Volvo | Antos 1832 | 60046, 60066, 60086, 60106, 60126 |
| `photo-1542282088-72c9c27ed0cd` | Volvo | TGX 18.510 | 60148, 60208 |
| `photo-1583121274602-3e2820c69888` | MAN | TGE 3.140 | 60155, 60185, 60215 |
| `photo-1541899481282-d53bffe3c35d` | MAN | Transporter T6.1 | 60053, 60083, 60113 |
| `photo-1583121274602-3e2820c69888` | Mercedes-Benz | Sprinter 316 CDI | 60165, 60195, 60225 |
| `photo-1541899481282-d53bffe3c35d` | Mercedes-Benz | Transporter T6.1 | 60063, 60093, 60123 |
| `photo-1583121274602-3e2820c69888` | Volkswagen | Crafter 35 | 60145, 60175, 60205, 60235 |
| `photo-1503376780353-7e6692767b70` | Volkswagen | Transporter T6.1 | 60004, 60034 |

## Candidats redondants forts proposés

| ID candidat | Représentant conservé provisoirement | Marque | Modèle | Année | Kilométrage | Catégorie | Preuve |
|---:|---:|---|---|---:|---:|---|---|
| 60231 | 60171 | Claas | 8R 410 | 2024 | 53000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60211 | 60151 | Claas | 933 Vario ProfiPlus | 2018 | 105000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60069 | 60049 | Claas | Axion 870 | 2020 | 121000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60089 | 60049 | Claas | Axion 870 | 2019 | 75000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60109 | 60049 | Claas | Axion 870 | 2018 | 29000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60129 | 60049 | Claas | Axion 870 | 2024 | 103000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60030 | 60010 | Claas | Axion 870 | 2020 | 121000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60079 | 60059 | John Deere | 8R 410 | 2023 | 38000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60099 | 60059 | John Deere | 8R 410 | 2022 | 112000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60119 | 60059 | John Deere | 8R 410 | 2021 | 66000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60139 | 60059 | John Deere | 8R 410 | 2020 | 20000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60221 | 60161 | John Deere | Axion 870 | 2021 | 24000 km | agricultural | même image normalisée + même identité déclarée; variations de données non probantes |
| 60137 | 60077 | MAN | Lion's Coach R08 | 2018 | 12600 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60179 | 60149 | MAN | Lion's Coach R08 | 2021 | 12200 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60209 | 60149 | MAN | Lion's Coach R08 | 2023 | 99200 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60107 | 60047 | MAN | Travego 15 SHD | 2023 | 21600 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60117 | 60057 | Mercedes-Benz | Lion's Coach R08 | 2019 | 58600 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60189 | 60159 | Mercedes-Benz | Travego 15 SHD | 2024 | 41200 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60219 | 60159 | Mercedes-Benz | Travego 15 SHD | 2019 | 18200 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150019 | 150009 | Mercedes-Benz / Setra | Iveco Crossway | 2019 | 50000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150029 | 150009 | Mercedes-Benz / Setra | Iveco Crossway | 2023 | 175000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150015 | 150005 | Mercedes-Benz / Setra | MAN Lion's | 2021 | 220000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150025 | 150005 | Mercedes-Benz / Setra | MAN Lion's | 2019 | 125000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150035 | 150005 | Mercedes-Benz / Setra | MAN Lion's | 2023 | 250000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150012 | 150002 | Mercedes-Benz / Setra | Mercedes-Benz Citaro | 2024 | 182500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150022 | 150002 | Mercedes-Benz / Setra | Mercedes-Benz Citaro | 2022 | 87500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150032 | 150002 | Mercedes-Benz / Setra | Mercedes-Benz Citaro | 2020 | 212500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150013 | 150003 | Mercedes-Benz / Setra | Mercedes-Benz Intouro | 2019 | 195000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150023 | 150003 | Mercedes-Benz / Setra | Mercedes-Benz Intouro | 2023 | 100000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150033 | 150003 | Mercedes-Benz / Setra | Mercedes-Benz Intouro | 2021 | 225000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150011 | 150001 | Mercedes-Benz / Setra | Mercedes-Benz Tourismo | 2023 | 170000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150021 | 150001 | Mercedes-Benz / Setra | Mercedes-Benz Tourismo | 2021 | 75000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150031 | 150001 | Mercedes-Benz / Setra | Mercedes-Benz Tourismo | 2019 | 200000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150016 | 150006 | Mercedes-Benz / Setra | Neoplan Tourliner | 2022 | 232500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150026 | 150006 | Mercedes-Benz / Setra | Neoplan Tourliner | 2020 | 137500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150036 | 150006 | Mercedes-Benz / Setra | Neoplan Tourliner | 2024 | 262500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150017 | 150007 | Mercedes-Benz / Setra | Scania Interlink | 2023 | 245000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150027 | 150007 | Mercedes-Benz / Setra | Scania Interlink | 2021 | 150000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150037 | 150007 | Mercedes-Benz / Setra | Scania Interlink | 2019 | 55000 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150014 | 150004 | Mercedes-Benz / Setra | Setra S | 2020 | 207500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150024 | 150004 | Mercedes-Benz / Setra | Setra S | 2024 | 112500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150034 | 150004 | Mercedes-Benz / Setra | Setra S | 2022 | 237500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150020 | 150010 | Mercedes-Benz / Setra | VDD Futura | 2020 | 62500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150030 | 150010 | Mercedes-Benz / Setra | VDD Futura | 2024 | 187500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150018 | 150008 | Mercedes-Benz / Setra | Volvo 9700 | 2024 | 257500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150028 | 150008 | Mercedes-Benz / Setra | Volvo 9700 | 2022 | 162500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 150038 | 150008 | Mercedes-Benz / Setra | Volvo 9700 | 2020 | 67500 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60199 | 60169 | Setra | Tourismo M | 2020 | 70200 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60229 | 60169 | Setra | Tourismo M | 2022 | 47200 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60127 | 60067 | Setra | Travego 15 SHD | 2022 | 95600 km | buses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60011 | 60001 | BMW | Série 3 | 2022 | 50700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60021 | 60001 | BMW | Série 3 | 2018 | 87700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60031 | 60001 | BMW | Série 3 | 2021 | 124700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60050 | 60040 | BMW | Série 3 | 2022 | 50700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60060 | 60040 | BMW | Série 3 | 2018 | 87700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60070 | 60040 | BMW | Série 3 | 2021 | 124700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60080 | 60040 | BMW | Série 3 | 2024 | 41700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60090 | 60040 | BMW | Série 3 | 2020 | 78700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60100 | 60040 | BMW | Série 3 | 2023 | 115700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60110 | 60040 | BMW | Série 3 | 2019 | 32700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60120 | 60040 | BMW | Série 3 | 2022 | 69700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60130 | 60040 | BMW | Série 3 | 2018 | 106700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60140 | 60040 | BMW | Série 3 | 2021 | 23700 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60142 | 30002 | BMW | Série 3 | 2019 | 14900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60152 | 30002 | BMW | Série 3 | 2022 | 43900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60162 | 30002 | BMW | Série 3 | 2018 | 72900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60172 | 30002 | BMW | Série 3 | 2021 | 101900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60182 | 30002 | BMW | Série 3 | 2024 | 20900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60192 | 30002 | BMW | Série 3 | 2020 | 49900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60202 | 30002 | BMW | Série 3 | 2023 | 78900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60212 | 30002 | BMW | Série 3 | 2019 | 107900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60222 | 30002 | BMW | Série 3 | 2022 | 26900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60232 | 30002 | BMW | Série 3 | 2018 | 55900 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 30001 | 1 | Mercedes-Benz | Classe C | 2022 | 38500 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 90011 | 90001 | Volkswagen | Golf VIII R | 2023 | 11000 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 120005 | 90005 | Volkswagen | Golf VIII R | 2023 | 16400 km | cars | même image normalisée + même identité déclarée; variations de données non probantes |
| 60043 | 3 | Volkswagen | Transporter T6.1 | 2022 | 24800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60073 | 3 | Volkswagen | Transporter T6.1 | 2024 | 15800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60103 | 3 | Volkswagen | Transporter T6.1 | 2019 | 126800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60133 | 3 | Volkswagen | Transporter T6.1 | 2021 | 117800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60227 | 60167 | BMW | 2000CS | 2020 | 41400 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60207 | 60147 | BMW | 300SL Gullwing | 2021 | 93400 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60065 | 60045 | BMW | 911 Turbo 3.3 | 2023 | 106200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60085 | 60045 | BMW | 911 Turbo 3.3 | 2022 | 60200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60105 | 60045 | BMW | 911 Turbo 3.3 | 2021 | 14200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60125 | 60045 | BMW | 911 Turbo 3.3 | 2020 | 88200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60026 | 60006 | BMW | 911 Turbo 3.3 | 2023 | 106200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60075 | 60055 | Mercedes-Benz | 911 Turbo 3.3 | 2019 | 23200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60095 | 60055 | Mercedes-Benz | 911 Turbo 3.3 | 2018 | 97200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60115 | 60055 | Mercedes-Benz | 911 Turbo 3.3 | 2024 | 51200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60135 | 60055 | Mercedes-Benz | 911 Turbo 3.3 | 2023 | 125200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60036 | 60016 | Mercedes-Benz | 911 Turbo 3.3 | 2019 | 23200 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60217 | 60157 | Mercedes-Benz | 911 Turbo 3.3 | 2024 | 12400 km | classics | même image normalisée + même identité déclarée; variations de données non probantes |
| 60122 | 60062 | Audi | M850i | 2024 | 77100 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60102 | 60042 | Audi | RS5 Coupé | 2018 | 123100 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60164 | 60144 | Audi | RS5 Coupé | 2020 | 78700 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60184 | 60144 | Audi | RS5 Coupé | 2019 | 26700 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60204 | 60144 | Audi | RS5 Coupé | 2018 | 84700 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60224 | 60144 | Audi | RS5 Coupé | 2024 | 32700 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60174 | 60154 | BMW | M4 Competition | 2023 | 107700 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60194 | 60154 | BMW | M4 Competition | 2022 | 55700 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60214 | 60154 | BMW | M4 Competition | 2021 | 113700 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60234 | 60154 | BMW | M4 Competition | 2020 | 61700 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60112 | 60052 | BMW | M4 Competition | 2021 | 40100 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60132 | 60072 | BMW | RS5 Coupé | 2020 | 114100 km | coupes | même image normalisée + même identité déclarée; variations de données non probantes |
| 60176 | 60156 | Audi | Taycan 4S | 2018 | 113500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60196 | 60156 | Audi | Taycan 4S | 2024 | 61500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60216 | 60156 | Audi | Taycan 4S | 2023 | 119500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60236 | 60156 | Audi | Taycan 4S | 2022 | 67500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60084 | 60054 | Audi | Taycan 4S | 2021 | 56500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60114 | 60054 | Audi | Taycan 4S | 2023 | 47500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60094 | 60064 | Audi | i4 M50 | 2024 | 93500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60124 | 60064 | Audi | i4 M50 | 2019 | 84500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60166 | 60146 | Audi | i4 M50 | 2022 | 84500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60186 | 60146 | Audi | i4 M50 | 2021 | 32500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60206 | 60146 | Audi | i4 M50 | 2020 | 90500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60226 | 60146 | Audi | i4 M50 | 2019 | 38500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60035 | 60005 | Audi | iX xDrive40 | 2018 | 19500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60074 | 60044 | Audi | iX xDrive40 | 2018 | 19500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60104 | 60044 | Audi | iX xDrive40 | 2020 | 10500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60134 | 60044 | Audi | iX xDrive40 | 2022 | 121500 km | electric | même image normalisée + même identité déclarée; variations de données non probantes |
| 60128 | 60068 | Ford | Crafter Transfer | 2023 | 99300 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60200 | 60170 | Ford | Crafter Transfer | 2021 | 73100 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60230 | 60170 | Ford | Crafter Transfer | 2023 | 50100 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60108 | 60048 | Mercedes-Benz | Crafter Transfer | 2024 | 25300 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60180 | 60150 | Mercedes-Benz | Crafter Transfer | 2022 | 15100 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60210 | 60150 | Mercedes-Benz | Crafter Transfer | 2024 | 102100 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60138 | 60078 | Mercedes-Benz | V-Class VIP | 2019 | 16300 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60190 | 60160 | Volkswagen | Crafter Transfer | 2018 | 44100 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60220 | 60160 | Volkswagen | Crafter Transfer | 2020 | 21100 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60118 | 60058 | Volkswagen | V-Class VIP | 2020 | 62300 km | minibuses | même image normalisée + même identité déclarée; variations de données non probantes |
| 60173 | 60153 | Audi | GLE 350d | 2022 | 104800 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60193 | 60153 | Audi | GLE 350d | 2021 | 52800 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60213 | 60153 | Audi | GLE 350d | 2020 | 110800 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60233 | 60153 | Audi | GLE 350d | 2019 | 58800 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60111 | 60071 | Audi | GLE 350d | 2020 | 36400 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60081 | 60041 | Audi | Q7 50 TDI | 2018 | 45400 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60121 | 60041 | Audi | Q7 50 TDI | 2023 | 73400 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60163 | 60143 | Audi | Q7 50 TDI | 2019 | 75800 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60183 | 60143 | Audi | Q7 50 TDI | 2018 | 23800 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60203 | 60143 | Audi | Q7 50 TDI | 2024 | 81800 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60223 | 60143 | Audi | Q7 50 TDI | 2023 | 29800 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60091 | 60051 | Audi | Touareg V6 | 2021 | 82400 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60131 | 60051 | Audi | Touareg V6 | 2019 | 110400 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60101 | 60061 | Audi | X3 xDrive20d | 2024 | 119400 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60141 | 60061 | Audi | X3 xDrive20d | 2022 | 27400 km | suvs | même image normalisée + même identité déclarée; variations de données non probantes |
| 60218 | 60158 | MAN | Arocs 3342 | 2018 | 15300 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60076 | 60056 | MAN | TGX 18.510 | 2020 | 26900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60096 | 60056 | MAN | TGX 18.510 | 2019 | 100900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60116 | 60056 | MAN | TGX 18.510 | 2018 | 54900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60136 | 60056 | MAN | TGX 18.510 | 2024 | 128900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60037 | 60017 | MAN | TGX 18.510 | 2020 | 26900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60228 | 60168 | Volvo | Actros 1845 LS | 2021 | 44300 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60027 | 60007 | Volvo | Antos 1832 | 2024 | 109900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60066 | 60046 | Volvo | Antos 1832 | 2024 | 109900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60086 | 60046 | Volvo | Antos 1832 | 2023 | 63900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60106 | 60046 | Volvo | Antos 1832 | 2022 | 17900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60126 | 60046 | Volvo | Antos 1832 | 2021 | 91900 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60208 | 60148 | Volvo | TGX 18.510 | 2022 | 96300 km | trucks | même image normalisée + même identité déclarée; variations de données non probantes |
| 60185 | 60155 | MAN | TGE 3.140 | 2020 | 29600 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60215 | 60155 | MAN | TGE 3.140 | 2022 | 116600 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60083 | 60053 | MAN | Transporter T6.1 | 2020 | 52800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60113 | 60053 | MAN | Transporter T6.1 | 2022 | 43800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60195 | 60165 | Mercedes-Benz | Sprinter 316 CDI | 2023 | 58600 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60225 | 60165 | Mercedes-Benz | Sprinter 316 CDI | 2018 | 35600 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60093 | 60063 | Mercedes-Benz | Transporter T6.1 | 2023 | 89800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60123 | 60063 | Mercedes-Benz | Transporter T6.1 | 2018 | 80800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60175 | 60145 | Volkswagen | Crafter 35 | 2024 | 110600 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60205 | 60145 | Volkswagen | Crafter 35 | 2019 | 87600 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60235 | 60145 | Volkswagen | Crafter 35 | 2021 | 64600 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |
| 60034 | 60004 | Volkswagen | Transporter T6.1 | 2024 | 15800 km | vans | même image normalisée + même identité déclarée; variations de données non probantes |

## Conflits catégorie ↔ photographie

Les **231 annonces** suivantes présentent une incompatibilité directe entre la catégorie déclarée et la photo visible (par exemple bus, camion, tracteur ou fourgonnette déclarés avec une photo de voiture). Elles sont des candidates prioritaires à la suppression ou à la révision, mais aucune action n’est appliquée automatiquement. La marque et le modèle exacts ne sont pas inventés.

| ID | Marque déclarée | Modèle déclaré | Catégorie | Type visuel visible | Image normalisée |
|---:|---|---|---|---|---|
| 60171 | Claas | 8R 410 | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60231 | Claas | 8R 410 | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60211 | Claas | 933 Vario ProfiPlus | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60151 | Claas | 933 Vario ProfiPlus | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60109 | Claas | Axion 870 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60089 | Claas | Axion 870 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60191 | Claas | Axion 870 | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60030 | Claas | Axion 870 | agricultural | unknown | `photo-1555215695-3004980ad54e` |
| 60069 | Claas | Axion 870 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60010 | Claas | Axion 870 | agricultural | unknown | `photo-1555215695-3004980ad54e` |
| 60049 | Claas | Axion 870 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60129 | Claas | Axion 870 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 30022 | Fendt | 724 Vario | agricultural | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 30021 | John Deere | 6R 250 | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60139 | John Deere | 8R 410 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60119 | John Deere | 8R 410 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60099 | John Deere | 8R 410 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60201 | John Deere | 8R 410 | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60079 | John Deere | 8R 410 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60020 | John Deere | 8R 410 | agricultural | unknown | `photo-1555215695-3004980ad54e` |
| 60059 | John Deere | 8R 410 | agricultural | unknown | `photo-1502877338535-766e1452684a` |
| 60181 | John Deere | 933 Vario ProfiPlus | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60221 | John Deere | Axion 870 | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60161 | John Deere | Axion 870 | agricultural | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 240017 | Branson | F50RN | agricultural-machinery | unknown | `photo-1563720223185-11003d516935` |
| 240005 | Case IH | Optum 300 | agricultural-machinery | unknown | `photo-1583121274602-3e2820c69888` |
| 240003 | Claas | Axion 870 | agricultural-machinery | unknown | `photo-1541899481282-d53bffe3c35d` |
| 240006 | Deutz-Fahr | Agrotron 9340 | agricultural-machinery | unknown | `photo-1525609004556-c46c7d6cf023` |
| 240001 | Fendt | Vario 942 | agricultural-machinery | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 240007 | JCB | Fastrac 8330 | agricultural-machinery | unknown | `photo-1563720223185-11003d516935` |
| 240002 | John Deere | 8R 410 | agricultural-machinery | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 240018 | Kioti | RX7320 | agricultural-machinery | unknown | `photo-1542282088-72c9c27ed0cd` |
| 240011 | Kubota | M7173 | agricultural-machinery | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 240014 | Lamborghini | Spire 100 | agricultural-machinery | unknown | `photo-1503376780353-7e6692767b70` |
| 240012 | Landini | Rex 4-120 | agricultural-machinery | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 240009 | Massey Ferguson | 8S.305 | agricultural-machinery | unknown | `photo-1502877338535-766e1452684a` |
| 240010 | McCormick | X8.680 | agricultural-machinery | unknown | `photo-1555215695-3004980ad54e` |
| 240004 | New Holland | T7.315 | agricultural-machinery | unknown | `photo-1503376780353-7e6692767b70` |
| 240013 | Same | Virtus 140 | agricultural-machinery | unknown | `photo-1541899481282-d53bffe3c35d` |
| 240019 | Solis | 90 N | agricultural-machinery | unknown | `photo-1502877338535-766e1452684a` |
| 240016 | Steyr | Terrus 6300 | agricultural-machinery | unknown | `photo-1525609004556-c46c7d6cf023` |
| 240008 | Valtra | S416 | agricultural-machinery | unknown | `photo-1542282088-72c9c27ed0cd` |
| 240015 | Zetor | Forterra 150 | agricultural-machinery | unknown | `photo-1583121274602-3e2820c69888` |
| 60137 | MAN | Lion's Coach R08 | buses | unknown | `photo-1563720223185-11003d516935` |
| 60149 | MAN | Lion's Coach R08 | buses | unknown | `photo-1502877338535-766e1452684a` |
| 60038 | MAN | Lion's Coach R08 | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60077 | MAN | Lion's Coach R08 | buses | unknown | `photo-1563720223185-11003d516935` |
| 60179 | MAN | Lion's Coach R08 | buses | unknown | `photo-1502877338535-766e1452684a` |
| 60209 | MAN | Lion's Coach R08 | buses | unknown | `photo-1502877338535-766e1452684a` |
| 60008 | MAN | Travego 15 SHD | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60047 | MAN | Travego 15 SHD | buses | unknown | `photo-1563720223185-11003d516935` |
| 60107 | MAN | Travego 15 SHD | buses | unknown | `photo-1563720223185-11003d516935` |
| 60117 | Mercedes-Benz | Lion's Coach R08 | buses | unknown | `photo-1563720223185-11003d516935` |
| 60018 | Mercedes-Benz | Lion's Coach R08 | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60057 | Mercedes-Benz | Lion's Coach R08 | buses | unknown | `photo-1563720223185-11003d516935` |
| 30017 | Mercedes-Benz | Tourismo 15 RHD | buses | unknown | `photo-1563720223185-11003d516935` |
| 60219 | Mercedes-Benz | Travego 15 SHD | buses | unknown | `photo-1502877338535-766e1452684a` |
| 60159 | Mercedes-Benz | Travego 15 SHD | buses | unknown | `photo-1502877338535-766e1452684a` |
| 60087 | Mercedes-Benz | Travego 15 SHD | buses | unknown | `photo-1563720223185-11003d516935` |
| 60189 | Mercedes-Benz | Travego 15 SHD | buses | unknown | `photo-1502877338535-766e1452684a` |
| 150019 | Mercedes-Benz / Setra | Iveco Crossway | buses | unknown | `photo-1502877338535-766e1452684a` |
| 150009 | Mercedes-Benz / Setra | Iveco Crossway | buses | unknown | `photo-1502877338535-766e1452684a` |
| 150029 | Mercedes-Benz / Setra | Iveco Crossway | buses | unknown | `photo-1502877338535-766e1452684a` |
| 150025 | Mercedes-Benz / Setra | MAN Lion's | buses | unknown | `photo-1583121274602-3e2820c69888` |
| 150015 | Mercedes-Benz / Setra | MAN Lion's | buses | unknown | `photo-1583121274602-3e2820c69888` |
| 150005 | Mercedes-Benz / Setra | MAN Lion's | buses | unknown | `photo-1583121274602-3e2820c69888` |
| 150035 | Mercedes-Benz / Setra | MAN Lion's | buses | unknown | `photo-1583121274602-3e2820c69888` |
| 150002 | Mercedes-Benz / Setra | Mercedes-Benz Citaro | buses | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 150032 | Mercedes-Benz / Setra | Mercedes-Benz Citaro | buses | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 150022 | Mercedes-Benz / Setra | Mercedes-Benz Citaro | buses | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 150012 | Mercedes-Benz / Setra | Mercedes-Benz Citaro | buses | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 150013 | Mercedes-Benz / Setra | Mercedes-Benz Intouro | buses | unknown | `photo-1541899481282-d53bffe3c35d` |
| 150003 | Mercedes-Benz / Setra | Mercedes-Benz Intouro | buses | unknown | `photo-1541899481282-d53bffe3c35d` |
| 150033 | Mercedes-Benz / Setra | Mercedes-Benz Intouro | buses | unknown | `photo-1541899481282-d53bffe3c35d` |
| 150023 | Mercedes-Benz / Setra | Mercedes-Benz Intouro | buses | unknown | `photo-1541899481282-d53bffe3c35d` |
| 150001 | Mercedes-Benz / Setra | Mercedes-Benz Tourismo | buses | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 150031 | Mercedes-Benz / Setra | Mercedes-Benz Tourismo | buses | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 150021 | Mercedes-Benz / Setra | Mercedes-Benz Tourismo | buses | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 150011 | Mercedes-Benz / Setra | Mercedes-Benz Tourismo | buses | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 150026 | Mercedes-Benz / Setra | Neoplan Tourliner | buses | unknown | `photo-1525609004556-c46c7d6cf023` |
| 150016 | Mercedes-Benz / Setra | Neoplan Tourliner | buses | unknown | `photo-1525609004556-c46c7d6cf023` |
| 150006 | Mercedes-Benz / Setra | Neoplan Tourliner | buses | unknown | `photo-1525609004556-c46c7d6cf023` |
| 150036 | Mercedes-Benz / Setra | Neoplan Tourliner | buses | unknown | `photo-1525609004556-c46c7d6cf023` |
| 150007 | Mercedes-Benz / Setra | Scania Interlink | buses | unknown | `photo-1563720223185-11003d516935` |
| 150037 | Mercedes-Benz / Setra | Scania Interlink | buses | unknown | `photo-1563720223185-11003d516935` |
| 150027 | Mercedes-Benz / Setra | Scania Interlink | buses | unknown | `photo-1563720223185-11003d516935` |
| 150017 | Mercedes-Benz / Setra | Scania Interlink | buses | unknown | `photo-1563720223185-11003d516935` |
| 150014 | Mercedes-Benz / Setra | Setra S | buses | unknown | `photo-1503376780353-7e6692767b70` |
| 150004 | Mercedes-Benz / Setra | Setra S | buses | unknown | `photo-1503376780353-7e6692767b70` |
| 150034 | Mercedes-Benz / Setra | Setra S | buses | unknown | `photo-1503376780353-7e6692767b70` |
| 150024 | Mercedes-Benz / Setra | Setra S | buses | unknown | `photo-1503376780353-7e6692767b70` |
| 150020 | Mercedes-Benz / Setra | VDD Futura | buses | unknown | `photo-1555215695-3004980ad54e` |
| 150010 | Mercedes-Benz / Setra | VDD Futura | buses | unknown | `photo-1555215695-3004980ad54e` |
| 150030 | Mercedes-Benz / Setra | VDD Futura | buses | unknown | `photo-1555215695-3004980ad54e` |
| 150008 | Mercedes-Benz / Setra | Volvo 9700 | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 150038 | Mercedes-Benz / Setra | Volvo 9700 | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 150028 | Mercedes-Benz / Setra | Volvo 9700 | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 150018 | Mercedes-Benz / Setra | Volvo 9700 | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60097 | Setra | Lion's Coach R08 | buses | unknown | `photo-1563720223185-11003d516935` |
| 30018 | Setra | S 515 HD | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60169 | Setra | Tourismo M | buses | unknown | `photo-1502877338535-766e1452684a` |
| 60199 | Setra | Tourismo M | buses | unknown | `photo-1502877338535-766e1452684a` |
| 60229 | Setra | Tourismo M | buses | unknown | `photo-1502877338535-766e1452684a` |
| 60028 | Setra | Travego 15 SHD | buses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60067 | Setra | Travego 15 SHD | buses | unknown | `photo-1563720223185-11003d516935` |
| 60127 | Setra | Travego 15 SHD | buses | unknown | `photo-1563720223185-11003d516935` |
| 60029 | Ford | Crafter Transfer | minibuses | unknown | `photo-1502877338535-766e1452684a` |
| 60068 | Ford | Crafter Transfer | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60170 | Ford | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60200 | Ford | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60128 | Ford | Crafter Transfer | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60230 | Ford | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60098 | Ford | V-Class VIP | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60009 | Mercedes-Benz | Crafter Transfer | minibuses | unknown | `photo-1502877338535-766e1452684a` |
| 60048 | Mercedes-Benz | Crafter Transfer | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60150 | Mercedes-Benz | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60180 | Mercedes-Benz | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60108 | Mercedes-Benz | Crafter Transfer | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60210 | Mercedes-Benz | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 30019 | Mercedes-Benz | Sprinter Transfer 45 | minibuses | unknown | `photo-1502877338535-766e1452684a` |
| 60138 | Mercedes-Benz | V-Class VIP | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60039 | Mercedes-Benz | V-Class VIP | minibuses | unknown | `photo-1502877338535-766e1452684a` |
| 60078 | Mercedes-Benz | V-Class VIP | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 30020 | Volkswagen | Crafter Minibus | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60088 | Volkswagen | Crafter Transfer | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60190 | Volkswagen | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60220 | Volkswagen | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60160 | Volkswagen | Crafter Transfer | minibuses | unknown | `photo-1555215695-3004980ad54e` |
| 60118 | Volkswagen | V-Class VIP | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60019 | Volkswagen | V-Class VIP | minibuses | unknown | `photo-1502877338535-766e1452684a` |
| 60058 | Volkswagen | V-Class VIP | minibuses | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60233 | Audi | GLE 350d | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60111 | Audi | GLE 350d | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60213 | Audi | GLE 350d | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60193 | Audi | GLE 350d | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60032 | Audi | GLE 350d | suvs | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 60071 | Audi | GLE 350d | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60173 | Audi | GLE 350d | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60153 | Audi | GLE 350d | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 30007 | Audi | Q7 | suvs | unknown | `photo-1563720223185-11003d516935` |
| 60081 | Audi | Q7 50 TDI | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60183 | Audi | Q7 50 TDI | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60163 | Audi | Q7 50 TDI | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60002 | Audi | Q7 50 TDI | suvs | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 60041 | Audi | Q7 50 TDI | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60143 | Audi | Q7 50 TDI | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60121 | Audi | Q7 50 TDI | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60223 | Audi | Q7 50 TDI | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60203 | Audi | Q7 50 TDI | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60131 | Audi | Touareg V6 | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60091 | Audi | Touareg V6 | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60012 | Audi | Touareg V6 | suvs | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 60051 | Audi | Touareg V6 | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60022 | Audi | X3 xDrive20d | suvs | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 60061 | Audi | X3 xDrive20d | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60141 | Audi | X3 xDrive20d | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60101 | Audi | X3 xDrive20d | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 30005 | BMW | X5 | suvs | unknown | `photo-1583121274602-3e2820c69888` |
| 180010 | Kia | Sportage | suvs | unknown | `photo-1555215695-3004980ad54e` |
| 30006 | Mercedes-Benz | GLE | suvs | unknown | `photo-1525609004556-c46c7d6cf023` |
| 180008 | Volkswagen | T-Roc | suvs | unknown | `photo-1542282088-72c9c27ed0cd` |
| 180005 | Volkswagen | T-Roc | suvs | unknown | `photo-1583121274602-3e2820c69888` |
| 180004 | Volkswagen | T-Roc | suvs | unknown | `photo-1503376780353-7e6692767b70` |
| 180006 | Volkswagen | T-Roc | suvs | unknown | `photo-1525609004556-c46c7d6cf023` |
| 180007 | Volkswagen | T-Roc | suvs | unknown | `photo-1563720223185-11003d516935` |
| 180003 | Volkswagen | T-Roc | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 180002 | Volkswagen | T-Roc | suvs | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 120002 | Volkswagen | Tiguan | suvs | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 120001 | Volkswagen | Tiguan | suvs | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 120004 | Volkswagen | Tiguan | suvs | unknown | `photo-1503376780353-7e6692767b70` |
| 120003 | Volkswagen | Tiguan | suvs | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60198 | MAN | Actros 1845 LS | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60218 | MAN | Arocs 3342 | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60158 | MAN | Arocs 3342 | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 30016 | MAN | TGM 18.290 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60116 | MAN | TGX 18.510 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60096 | MAN | TGX 18.510 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60037 | MAN | TGX 18.510 | trucks | unknown | `photo-1563720223185-11003d516935` |
| 60076 | MAN | TGX 18.510 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60178 | MAN | TGX 18.510 | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60017 | MAN | TGX 18.510 | trucks | unknown | `photo-1563720223185-11003d516935` |
| 60056 | MAN | TGX 18.510 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60136 | MAN | TGX 18.510 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 240024 | Mercedes-Benz | Actros 1853 L | trucks | unknown | `photo-1503376780353-7e6692767b70` |
| 30015 | Mercedes-Benz | Atego 1224 | trucks | unknown | `photo-1583121274602-3e2820c69888` |
| 240025 | Renault | T High Turbo Compound | trucks | unknown | `photo-1583121274602-3e2820c69888` |
| 240027 | Renault | T480 Sleeper | trucks | unknown | `photo-1563720223185-11003d516935` |
| 240023 | Scania | R770 V8 | trucks | unknown | `photo-1541899481282-d53bffe3c35d` |
| 240022 | Scania | S660 Highline | trucks | unknown | `photo-1603584173870-7f23fdae1b7a` |
| 60228 | Volvo | Actros 1845 LS | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60168 | Volvo | Actros 1845 LS | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60007 | Volvo | Antos 1832 | trucks | unknown | `photo-1563720223185-11003d516935` |
| 60046 | Volvo | Antos 1832 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60126 | Volvo | Antos 1832 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60106 | Volvo | Antos 1832 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60086 | Volvo | Antos 1832 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60027 | Volvo | Antos 1832 | trucks | unknown | `photo-1563720223185-11003d516935` |
| 60066 | Volvo | Antos 1832 | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 60188 | Volvo | Arocs 3342 | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 240026 | Volvo | FH Globetrotter | trucks | unknown | `photo-1525609004556-c46c7d6cf023` |
| 240020 | Volvo | FH16 750 | trucks | unknown | `photo-1555215695-3004980ad54e` |
| 240028 | Volvo | FH16 Aero | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 240021 | Volvo | FMX 540 Dumper | trucks | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60148 | Volvo | TGX 18.510 | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60208 | Volvo | TGX 18.510 | trucks | unknown | `photo-1542282088-72c9c27ed0cd` |
| 60155 | MAN | TGE 3.140 | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60185 | MAN | TGE 3.140 | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60215 | MAN | TGE 3.140 | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60014 | MAN | Transporter T6.1 | vans | unknown | `photo-1503376780353-7e6692767b70` |
| 60053 | MAN | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60083 | MAN | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60113 | MAN | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60225 | Mercedes-Benz | Sprinter 316 CDI | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60165 | Mercedes-Benz | Sprinter 316 CDI | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60195 | Mercedes-Benz | Sprinter 316 CDI | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 30011 | Mercedes-Benz | Sprinter 319 | vans | unknown | `photo-1618843479313-40f8afb4b4d8` |
| 60123 | Mercedes-Benz | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60024 | Mercedes-Benz | Transporter T6.1 | vans | unknown | `photo-1503376780353-7e6692767b70` |
| 60063 | Mercedes-Benz | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60093 | Mercedes-Benz | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60205 | Volkswagen | Crafter 35 | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60235 | Volkswagen | Crafter 35 | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60145 | Volkswagen | Crafter 35 | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60175 | Volkswagen | Crafter 35 | vans | unknown | `photo-1583121274602-3e2820c69888` |
| 60103 | Volkswagen | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 30010 | Volkswagen | Transporter T6.1 | vans | unknown | `photo-1555215695-3004980ad54e` |
| 60133 | Volkswagen | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60004 | Volkswagen | Transporter T6.1 | vans | unknown | `photo-1503376780353-7e6692767b70` |
| 60043 | Volkswagen | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |
| 60034 | Volkswagen | Transporter T6.1 | vans | unknown | `photo-1503376780353-7e6692767b70` |
| 60073 | Volkswagen | Transporter T6.1 | vans | unknown | `photo-1541899481282-d53bffe3c35d` |

## Décision requise

Ce document est une proposition de revue. Il ne supprime rien et ne change aucune annonce. Une suppression ne devrait être exécutée qu’après validation explicite des groupes et des IDs.

