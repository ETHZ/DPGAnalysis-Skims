import FWCore.ParameterSet.Config as cms
hltstoppedhscp = cms.EDFilter("HLTHighLevel",
                                      TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
                                      HLTPaths = cms.vstring("HLT_StoppedHSCP*"), # provide list of HLT paths (or patterns) you want
                                      eventSetupPathsKey = cms.string(''), # not empty => use read paths from AlCaRecoTriggerBitsRcd via this key
                                      andOr = cms.bool(True),             # how to deal with multiple triggers: True (OR) accept if ANY is true, False (AND) accept if ALL are true
                                      throw = cms.bool(False)    # throw exception on unknown path names
 )

HSCPSkim =cms.Sequence(process.hltstoppedhscp)

