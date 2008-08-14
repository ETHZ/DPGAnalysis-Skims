import FWCore.ParameterSet.Config as cms

#------------------------------------------
# parameters for the CSCSkim module
#------------------------------------------
cscSkim = cms.EDFilter("CSCSkim",
    typeOfSkim         = cms.untracked.int32(1),
    rootFileName       = cms.untracked.string('outputDummy.root'),
    histogramFileName  = cms.untracked.string('CSCSkim_histos.root'),
    nLayersWithHitsMinimum  = cms.untracked.int32(3),
    minimumHitChambers      = cms.untracked.int32(3),
    minimumSegments         = cms.untracked.int32(2),
    demandChambersBothSides = cms.untracked.bool(False),
    makeHistograms          = cms.untracked.bool(False)
)

#
