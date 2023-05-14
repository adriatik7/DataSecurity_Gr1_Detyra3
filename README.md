# DataSecurity_Gr1_Detyra3

Grupi 1: Adrian Sopi, Adriatik Krasniqi, Agnesa Jashanica, Armela Hajra 

Programimi i punes se SBox-eve dhe fitimi i 16 SubKey per secilin round te Algoritmit DES

Data Encryption Standard (DES) eshte block cipher 64 bitesh me 16 raunde dhe çeles me gjatesi prej 56 bitesh.
Ky projekt implementon Algoritmin DES (Data Encryption Standard) për kriptimin e të dhënave. 
Për të realizuar këtë, përdorim dy pjesë kryesore të algoritmit: S-box-et dhe fitimin e 16 SubKey për secilin raund.

S-box-et janë tabele lookup që ndryshojnë vlerat e bllokëve të dhënave. S-box-et përdoren për të zëvendësuar pjesët e caktuara të bllokëve të dhënave me vlera të reja, duke bërë kriptimin më të fortë dhe më të sigurt. 
Përdorimi i listave direkt lookup është një metodë efikase për të gjetur vlerën e përshtatshme në S-box, duke ndihmuar në performancën e algoritmit tonë.

Fitimi i 16 SubKey: Çelësi origjinal i kodimit i ndahet në 16 nënçelesa të ndryshëm, të njohur si SubKey, për të përdorur në secilin raund të kodimit. Këto nënçelesa fitohen duke i aplikuar transformime dhe permutime të caktuara në çelësin origjinal. 
Ne kemi implementuar logjikën për të fituar këto 16 SubKey dhe i përdorim ato për të kriptuar dhe dekriptuar tekstin e dhënë. Ky proces ndihmon në ndarjen e punës së kodimit në raunde dhe rrit nivelin e sigurisë së algoritmit.

Përdorimi i këtij projekti ju mundëson të shfrytëzoni Algoritmin DES për qëllime të sigurisë dhe kriptografisë. Ju mund ta përdorni këtë program për të zhvilluar dhe testuar algoritmin DES në mënyrë të thjeshtë dhe efikase.
