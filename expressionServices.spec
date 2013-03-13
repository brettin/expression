module ExpressionServices { 

    /* KBase Feature ID for a feature, typically CDS/PEG */
    typedef string FeatureID;
    
    /* KBase list of Feature IDs , typically CDS/PEG */
    typedef list<FeatureID> FeatureIDs;
    
    /* Log2Level (Zero median normalized within a sample) for a given feature */
    typedef float Log2Level;
    
    /* KBase Sample ID for the sample */
    typedef string SampleID;
    
    /* List of KBase Sample IDs */
    typedef list<SampleID> SampleIDs;
    
    /* Sample type controlled vocabulary : microarray, RNA-Seq, qPCR, or proteomics */
    typedef string SampleType;
    
    /* Kbase Series Id */ 
    typedef string SeriesID; 
    
    /* list of KBase Series Ids */
    typedef list<SeriesID> SeriesIDs;
    
    /* Kbase ExperimentMeta Id */ 
    typedef string ExperimentMetaID; 
    
    /* list of KBase ExperimentMeta Ids */
    typedef list<ExperimentMetaID> ExperimentMetaIDs;
    
    /* Kbase ExperimentalUnitId */ 
    typedef string ExperimentalUnitID; 
    
    /* list of KBase ExperimentUnitIds */
    typedef list<ExperimentalUnitID> ExperimentalUnitIDs;
    
    /* mapping kbase feature id as the key and log2level as the value */
    typedef mapping<FeatureID feature_id, Log2Level log2level> DataExpressionLevelsForSample; 
    
    /* Kbase SampleAnnotation Id */ 
    typedef string SampleAnnotationID; 
    
    /* list of KBase SampleAnnotation Ids */
    typedef list<SampleAnnotationID> SampleAnnotationIDs;
    
    /* Kbase Person Id */ 
    typedef string PersonID; 
    
    /* list of KBase PersonsIds */
    typedef list<PersonID> PersonIDs;
    
    /* KBase StrainId */
    typedef string StrainID;
    
    /* list of KBase StrainIds */
    typedef list<StrainID> StrainIDs;
    
    /* KBase GenomeId */
    typedef string GenomeID;
    
    /* list of KBase GenomeIds */
    typedef list<GenomeID> GenomeIDs;
    
    /* Single integer 1= WildTypeonly, 0 means all strains ok */
    typedef int WildTypeOnly;
    
    /* Data structure for all the top level metadata and value data for an expression sample */
    typedef structure {
	SampleID sampleId;
	string sourceId;
	string sampleTitle;
	string sampleDescription;
	string molecule;
	SampleType sampleType;
	string dataSource;
	string externalSourceId;
	string externalSourceDate;
	string kbaseSubmissionDate;
	string custom;
	float originalLog2Median;
	StrainID strainID;
	string referenceStrain;
	string wildtype;
	string strainDescription;
	GenomeID genomeID;
	string genomeScientificName;
	string platformId;
	string platformTitle;
	string platformTechnology;
	ExperimentalUnitID experimentalUnitID;
	ExperimentMetaID experimentMetaID;
	string experimentTitle;
	string experimentDescription;
	string environmentId;
	string environmentDescription;
	string protocolId;
	string protocolDescription;
	string protocolName;
	SampleAnnotationIDs sampleAnnotationIDs;
	SeriesIDs seriesIds;
	PersonIDs personIds;
	DataExpressionLevelsForSample dataExpressionLevelsForSample;
	} ExpressionDataSample;
    
    /* Mapping between sampleId and ExpressionDataSample */
    typedef mapping<SampleID sampleId, ExpressionDataSample> ExpressionDataSamplesMap;
    
    /*mapping between seriesIds and all Samples it contains*/
    typedef mapping<SeriesID series_id, ExpressionDataSamplesMap> SeriesExpressionDataSamplesMapping;
    
    /*mapping between experimentalUnitIds and all Samples it contains*/
    typedef mapping<ExperimentalUnitID experimentalUnitID, ExpressionDataSamplesMap> ExperimentalUnitExpressionDataSamplesMapping;

    /*mapping between experimentMetaIds and ExperimentalUnitExpressionDataSamplesMapping it contains*/
    typedef mapping<ExperimentMetaID experimentMetaID, ExperimentalUnitExpressionDataSamplesMapping> ExperimentMetaExpressionDataSamplesMapping;
    
    /*mapping between strainIds and all Samples it contains*/
    typedef mapping<StrainID strainID, ExpressionDataSamplesMap> StrainExpressionDataSamplesMapping;

    /*mapping between genomeIds and all StrainExpressionDataSamplesMapping it contains*/
    typedef mapping<GenomeID genomeID, StrainExpressionDataSamplesMapping> GenomeExpressionDataSamplesMapping;

    /* mapping kbase sample id as the key and a single log2level (for a scpecified feature id, one mapping higher) as the value */
    
    typedef mapping<SampleID sampled, Log2Level log2level> SampleLog2LevelMapping; 
    
    /*mapping between FeatureIds and the mappings between samples and log2level mapping*/
    typedef mapping<FeatureID featureId, SampleLog2LevelMapping sampleLog2LevelMapping> FeatureSampleLog2LevelMapping;

    /*FUNCTIONS*/
    
    /* core function used by many others.  Given a list of SampleIds returns mapping of SampleId to SampleDataStructure */
    funcdef get_expression_samples_data(SampleIDs sampleIds) returns (ExpressionDataSamplesMap expressionDataSamplesMap);

    /* given a list of SeriesIds returns mapping of SeriesId to expressionDataSamples */
    funcdef get_expression_samples_data_by_series_ids(SeriesIDs seriesIds) returns (SeriesExpressionDataSamplesMapping seriesExpressionDataSamplesMapping);
    
    /* given a list of ExperimentalUnitIds returns mapping of ExperimentalUnitId to expressionDataSamples */
    funcdef get_expression_samples_data_by_experimental_unit_ids(ExperimentalUnitIDs experimentalUnitIDs) returns (ExperimentalUnitExpressionDataSamplesMapping experimentalUnitExpressionDataSamplesMapping);
    
    /* given a list of ExperimentMetaIds returns mapping of ExperimentId to experimentalUnitExpressionDataSamplesMapping */
    funcdef get_expression_experimental_unit_samples_data_by_experiment_meta_ids(ExperimentMetaIDs experimentMetaIDs) returns (ExperimentMetaExpressionDataSamplesMapping experimentMetaExpressionDataSamplesMapping);
    
    /* given a list of Strains, and a SampleType, it returns a StrainExpressionDataSamplesMapping,  StrainId -> ExpressionDataSample*/
    funcdef get_expression_samples_data_by_strain_ids(StrainIDs strainIDs, SampleType sampleType) returns (StrainExpressionDataSamplesMapping strainExpressionDataSamplesMapping);

    /* given a list of Genomes, a SampleType and a int indicating WildType Only (1 = true, 0 = false) , it returns a GenomeExpressionDataSamplesMapping   ,  Genome -> StrainId -> ExpressionDataSample*/
    funcdef get_expression_samples_data_by_genome_ids(GenomeIDs genomeIDs, SampleType sampleType, WildTypeOnly wildTypeOnly) returns (GenomeExpressionDataSamplesMapping genomeExpressionDataSamplesMapping);

    /* given a list of FeatureIds, a SampleType and a int indicating WildType Only (1 = true, 0 = false) returns a FeatureSampleLog2LevelMapping : featureId->{sample_id->log2Level} */
    funcdef get_expression_data_by_feature_ids(FeatureIDs featureIds, SampleType sampleType, WildTypeOnly wildTypeOnly) returns (FeatureSampleLog2LevelMapping featureSampleLog2LevelMapping);
    
}; 
