# Komunikim Klient-Server me TCP Certifikata_digjitaleX509

Ky projekt demonstron një aplikacion komunikimi klient-server duke përdorur protokollin TCP. Në këtë aplikacion, të dhënat që transmetohen mes klientit dhe serverit janë të kriptuara dhe të nënshkruara në mënyrë digjitale, duke përdorur teknologjinë e certifikatave X.509. Kriptimi siguron që të dhënat e dërguara janë të mbrojtura nga ndërhyrjet e paautorizuara gjatë transmetimit, ndërsa nënshkrimi digjital garanton integritetin dhe autentikimin e të dhënave, duke siguruar që mesazhet nuk janë manipuluar dhe vërtetojnë identitetin e dërguesit.

Protokolli TCP përdoret për të garantuar një lidhje të besueshme dhe të orientuar drejt lidhjes midis klientit dhe serverit. Certifikatat X.509, të cilat janë standard për infrastrukturën e çelësave publikë (PKI), përdoren për të menaxhuar çelësat kriptografikë dhe për të nënshkruar mesazhet në mënyrë digjitale. Në këtë mënyrë, të dhënat janë jo vetëm të koduara për të parandaluar dëgjimin e tyre nga palët e treta, por gjithashtu janë të pajisura me nënshkrime digjitale për të siguruar që dërguesi i të dhënave është autentik dhe se përmbajtja e të dhënave është e paprekur.

Ky aplikacion demonstron praktika të mira në sigurimin e komunikimeve përmes internetit, duke përfshirë përdorimin e çelësave publikë dhe privatë për kriptim dhe nënshkrim digjital. Çelësi publik i serverit përdoret nga klienti për të kriptuar mesazhet, dhe vetëm serveri që posedon çelësin privat të përkatësishëm mund të dekriptojë këto mesazhe. Po ashtu, çelësi privat i klientit përdoret për të nënshkruar mesazhet, ndërsa serveri përdor çelësin publik të klientit për të verifikuar nënshkrimin.

Në përmbledhje, ky projekt ilustron se si të sigurohet një komunikim i sigurt dhe i besueshëm ndërmjet një klienti dhe një serveri duke përdorur protokollin TCP dhe certifikatat X.509 për kriptimin dhe nënshkrimin digjital të të dhënave.


## Antaret e grupit
### -Andi Ternava
### -Alisa Shala
### -Amir Balje
### -Arbana Neziraj

