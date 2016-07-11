#!/bin/bash
initialFolder=${PWD}
for mass in 80 100 120 140 160 180 200 220 240 260 280 300 350 400 450 500 550 600 650 700 750 800 850 900 950 1000 1100 1200 1300 1400 1500
do
	NAME=RPVStopStopToJets_UDD323_M-${mass}
	workingDir=${initialFolder}/calcFilterEff/${NAME}
	echo "Creating Folder and Files "$workingDir 
	if [ ! -d $workingDir ]; then
		mkdir -p $workingDir
	fi
	cp ${initialFolder}/step0_LHE_v7124.py ${workingDir}/step00_${NAME}_LHE_cfg.py
	cp ${initialFolder}/step0_GEN_SIM_v7124.py ${workingDir}/step01_${NAME}_GENSIM_cfg.py
	sed -i 's/HadRPVStop100_UDD312_13TeV_LHE.root/'"${NAME}"'_LHE.root/' ${workingDir}/step00_${NAME}_LHE_cfg.py 
	sed -i 's/HadRPVStop100_UDD312_13TeV_tarball.tar.xz/HadRPVStop'"${mass}"'_UDD323_13TeV_tarball.tar.xz/' ${workingDir}/step00_${NAME}_LHE_cfg.py 
	sed -i 's/HadRPVStop100_UDD312_13TeV_LHE.root/'"${NAME}"'_LHE.root/' ${workingDir}/step01_${NAME}_GENSIM_cfg.py 
	sed -i 's/HadRPVStop100_UDD312_13TeV_GENSIM.root/'"${NAME}"'_GENSIM.root/' ${workingDir}/step01_${NAME}_GENSIM_cfg.py 
	if [ ${mass} -gt 290 ]; then
		sed -i 's/process.ProductionFilterSequence = cms.Sequence(process.generator+process.htFilter)/process.ProductionFilterSequence = cms.Sequence(process.generator)/' ${workingDir}/step01_${NAME}_GENSIM_cfg.py
	fi
	cd ${workingDir}
	echo "Running LHE"
	cmsRun step00_${NAME}_LHE_cfg.py &> lhe.log; cmsRun step01_${NAME}_GENSIM_cfg.py &> gen.log; 
	cd ${initialFolder}
done
