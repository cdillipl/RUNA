# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/DM_ScalarZH_Mphi-2000_Mchi-50_gSM-1p0_gDM-1p0_13TeV-JHUGen/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/AODSIM --fileout file:EXO-RunIISpring15MiniAODv2-00903.root --mc --eventcontent MINIAODSIM --runUnscheduled --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 74X_mcRun2_asymptotic_v2 --step PAT --python_filename /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/EXO-RunIISpring15MiniAODv2-00903/EXO-RunIISpring15MiniAODv2-00903_1_cfg.py --no_exec -n 1920
import FWCore.ParameterSet.Config as cms

process = cms.Process('PAT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1920)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_1.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_10.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_100.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_101.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_102.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_103.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_104.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_105.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_106.root',
	    '/store/user/algomez/RPVSt100tojj_13TeV_pythia8/RunIISpring15DR74_AODSIM_Asympt25ns/150715_204635/0000/RPVSt100tojj_13TeV_pythia8_AODSIM_Asympt25ns_107.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:1920'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:EXO-RunIISpring15MiniAODv2-00903.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideInputFileSplitLevels = cms.untracked.bool(True)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '74X_mcRun2_asymptotic_v2', '')

# Path and EndPath definitions
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)
process.load('Configuration.StandardSequences.PATMC_cff')
from FWCore.ParameterSet.Utilities import cleanUnscheduled
process=cleanUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions
