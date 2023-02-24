# ----------------------------------------------------------------------------
# Copyright (c) 2016-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

MAP_2023 = {
    # 2023.2 DISTRO
    'distro/core/qiime2-2023.2-py38-osx-conda.yml':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2023.2/release/qiime2-2023.2-py38-osx-conda.yml',
    'distro/core/qiime2-2023.2-py38-linux-conda.yml':
        'https://raw.githubusercontent.com/qiime2/environment-files/master/2023.2/release/qiime2-2023.2-py38-linux-conda.yml',
    'distro/core/2023.2':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/distro/core/qiime20232-{BUILDID}.zip',
    'distro/core/qiime20232-{BUILDID}.zip':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/distro/core/qiime20232-{BUILDID}.zip',

    # 2023.2
    '2023.2/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2023.2/common/gg-13-8-99-515-806-nb-weighted-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/gg-13-8-99-515-806-nb-weighted-classifier.qza',
    '2023.2/common/gg-13-8-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/gg-13-8-99-nb-classifier.qza',
    '2023.2/common/gg-13-8-99-nb-weighted-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/gg-13-8-99-nb-weighted-classifier.qza',
    '2023.2/common/sepp-refs-gg-13-8.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/sepp-refs-gg-13-8.qza',
    '2023.2/common/sepp-refs-silva-128.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/sepp-refs-silva-128.qza',
    '2023.2/common/silva-138-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/silva-138-99-515-806-nb-classifier.qza',
    '2023.2/common/silva-138-99-515-806-nb-weighted-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/silva-138-99-515-806-nb-weighted-classifier.qza',
    '2023.2/common/silva-138-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/silva-138-99-nb-classifier.qza',
    '2023.2/common/silva-138-99-nb-weighted-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/common/silva-138-99-nb-weighted-classifier.qza',
    '2023.2/common/silva-138-99-seqs-515-806.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/common/silva-138-99-seqs-515-806.qza',
    '2023.2/common/silva-138-99-seqs.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/common/silva-138-99-seqs.qza',
    '2023.2/common/silva-138-99-tax-515-806.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/common/silva-138-99-tax-515-806.qza',
    '2023.2/common/silva-138-99-tax.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/common/silva-138-99-tax.qza',
    '2023.2/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/atacama-soils/10p/barcodes.fastq.gz',
    '2023.2/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/atacama-soils/10p/forward.fastq.gz',
    '2023.2/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/atacama-soils/10p/reverse.fastq.gz',
    '2023.2/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/atacama-soils/1p/barcodes.fastq.gz',
    '2023.2/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/atacama-soils/1p/forward.fastq.gz',
    '2023.2/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/atacama-soils/1p/reverse.fastq.gz',
    '2023.2/tutorials/chimera/atacama-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/chimera/atacama-table.qza',
    '2023.2/tutorials/chimera/atacama-rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/chimera/atacama-rep-seqs.qza',
    '2023.2/tutorials/exporting/feature-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/exporting/feature-table.qza',
    '2023.2/tutorials/exporting/unrooted-tree.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/exporting/unrooted-tree.qza',
    '2023.2/tutorials/filtering/distance-matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/filtering/distance-matrix.qza',
    '2023.2/tutorials/filtering/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/filtering/table.qza',
    '2023.2/tutorials/filtering/taxonomy.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/filtering/taxonomy.qza',
    '2023.2/tutorials/filtering/sequences.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/filtering/sequences.qza',
    '2023.2/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2023.2/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2023.2/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2023.2/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2023.2/tutorials/fmt-cdiff-khanna/manifest.csv':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/fmt-cdiff-khanna/manifest.csv',
    '2023.2/tutorials/fmt-cdiff-khanna/sequence_files.zip':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/fmt-cdiff-khanna/sequence_files.zip',
    '2023.2/tutorials/gneiss/sample-metadata.tsv':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/gneiss/sample-metadata.tsv',
    '2023.2/tutorials/gneiss/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/gneiss/table.qza',
    '2023.2/tutorials/gneiss/taxa.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/gneiss/taxa.qza',
    '2023.2/tutorials/importing/aligned-sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/aligned-sequences.fna',
    '2023.2/tutorials/importing/casava-18-paired-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/casava-18-paired-end-demultiplexed.zip',
    '2023.2/tutorials/importing/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/casava-18-single-end-demultiplexed.zip',
    '2023.2/tutorials/importing/feature-table-v100.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/feature-table-v100.biom',
    '2023.2/tutorials/importing/feature-table-v210.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/feature-table-v210.biom',
    '2023.2/tutorials/importing/muxed-se-barcode-in-seq.fastq.gz':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/importing/muxed-se-barcode-in-seq.fastq.gz',
    '2023.2/tutorials/importing/pe-64-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/pe-64-manifest',
    '2023.2/tutorials/importing/pe-64.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/pe-64.zip',
    '2023.2/tutorials/importing/se-33-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/se-33-manifest',
    '2023.2/tutorials/importing/se-33.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/se-33.zip',
    '2023.2/tutorials/importing/sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/sequences.fna',
    '2023.2/tutorials/importing/unrooted-tree.tre':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/unrooted-tree.tre',
    '2023.2/tutorials/importing/muxed-pe-barcode-in-seq/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/muxed-pe-barcode-in-seq/forward.fastq.gz',
    '2023.2/tutorials/importing/muxed-pe-barcode-in-seq/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/importing/muxed-pe-barcode-in-seq/reverse.fastq.gz',
    '2023.2/tutorials/longitudinal/ecam_table_taxa.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/longitudinal/ecam_table_taxa.qza',
    '2023.2/tutorials/longitudinal/ecam_shannon.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/longitudinal/ecam_shannon.qza',
    '2023.2/tutorials/longitudinal/unweighted_unifrac_distance_matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/longitudinal/unweighted_unifrac_distance_matrix.qza',
    '2023.2/tutorials/longitudinal/ecam_table_maturity.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/longitudinal/ecam_table_maturity.qza',
    '2023.2/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz',
    '2023.2/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz',
    '2023.2/tutorials/metadata/faith_pd_vector.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/metadata/faith_pd_vector.qza',
    '2023.2/tutorials/metadata/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/metadata/rep-seqs.qza',
    '2023.2/tutorials/metadata/taxonomy.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/metadata/taxonomy.qza',
    '2023.2/tutorials/metadata/unweighted_unifrac_pcoa_results.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/metadata/unweighted_unifrac_pcoa_results.qza',
    '2023.2/tutorials/otu-clustering/seqs.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/otu-clustering/seqs.fna',
    '2023.2/tutorials/otu-clustering/85_otus.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/otu-clustering/85_otus.qza',
    '2023.2/tutorials/pd-mice/animal_distal_gut.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/pd-mice/animal_distal_gut.qza',
    '2023.2/tutorials/pd-mice/demultiplexed_seqs.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/pd-mice/demultiplexed_seqs.zip',
    '2023.2/tutorials/pd-mice/manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/pd-mice/manifest',
    '2023.2/tutorials/pd-mice/ref_seqs_v4.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/pd-mice/ref_seqs_v4.qza',
    '2023.2/tutorials/pd-mice/ref_tax.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/pd-mice/ref_tax.qza',
    '2023.2/tutorials/quality-control/qc-mock-3-expected.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/quality-control/qc-mock-3-expected.qza',
    '2023.2/tutorials/quality-control/qc-mock-3-observed.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/quality-control/qc-mock-3-observed.qza',
    '2023.2/tutorials/quality-control/query-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/quality-control/query-seqs.qza',
    '2023.2/tutorials/quality-control/reference-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/quality-control/reference-seqs.qza',
    '2023.2/tutorials/quality-control/query-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/quality-control/query-table.qza',
    '2023.2/tutorials/read-joining/atacama-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/read-joining/atacama-seqs.qza',
    '2023.2/tutorials/read-joining/fj-joined.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/read-joining/fj-joined.zip',
    '2023.2/tutorials/sample-classifier/atacama-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/sample-classifier/atacama-table.qza',
    '2023.2/tutorials/sample-classifier/moving-pictures-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/sample-classifier/moving-pictures-table.qza',
    '2023.2/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2023.2/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/training-feature-classifiers/85_otus.fasta',
    '2023.2/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2023.2/tutorials/training-feature-classifiers/rep-seqs.qza',
    '2023.2/tutorials/phylogeny/rep-seqs.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/phylogeny/rep-seqs.qza',
    '2023.2/tutorials/utilities/faith-pd-vector.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/utilities/faith-pd-vector.qza',
    '2023.2/tutorials/utilities/jaccard-pcoa.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/utilities/jaccard-pcoa.qza',
    '2023.2/tutorials/utilities/taxa-barplot.qzv':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2023.2/tutorials/utilities/taxa-barplot.qzv',
    '2023.2/tutorials/liao/fmt-metadata.tsv':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2023.2/tutorials/liao/fmt-metadata.tsv',
    '2023.2/tutorials/liao/sample-metadata.tsv':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2023.2/tutorials/liao/sample-metadata.tsv',
    '2023.2/tutorials/liao/transplant-metadata.tsv':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2023.2/tutorials/liao/transplant-metadata.tsv',
    '2023.2/tutorials/liao/rep-seqs.qza':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2023.2/tutorials/liao/rep-seqs.qza',
    '2023.2/tutorials/liao/full-feature-table.qza':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2023.2/tutorials/liao/full-feature-table.qza',
    '2023.2/tutorials/liao/fastq-casava.zip':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2023.2/tutorials/liao/fastq-casava.zip',

    # Sample Metadata (hosted on Google Sheets)
    ## All of the following tutorials use the *new* docs sharing menu, via "File -> Publish to the Web" dialog for TSV export.

    ## FMT
    '2023.2/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/15dbbxb8T7cZ3iHBsS4511IVWVE4-vwC6yG-v0Cyn8js/edit?usp=sharing',
    '2023.2/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vSuwSudEIC-gUBR7pVakJSc7461a1fjRP543jitwNczNTEJoHALr-i25FyWb8aHu9lizRsbnBZlPMPN/pub?gid=0&single=true&output=tsv',

    ## Moving Pictures
    '2023.2/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1I9TzFqkjQ9RvXMrP7StbWwMid5pjFN8exYC7nUVpKFs/edit?usp=sharing',
    '2023.2/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vTDeMqrgOV0OAB8XUJnS_1ULbIgAIbEUuaM5MMGnx8B2S0QzBgYSwPsKw_O_KzZ9rC50IcgIcc4924S/pub?gid=0&single=true&output=tsv',

    ## Atacama
    '2023.2/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1bnsQ8ECdfnSBr0VjBiT2RLOn5WH6Uf5i6I06zJjXaEA/edit?usp=sharing',
    '2023.2/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vQDdJGnw-zyj-xUwkWiUVpRTbVry9d8tUKGkwQ5o6TrH6gypxeIJ6nNnju54_KZq51eahbddyFyGrhT/pub?gid=0&single=true&output=tsv',

    ## Longitudinal
    '2023.2/tutorials/longitudinal/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1BeS5mi1f-y_tUhZbibexhCmRkAGjFpPnPrfxT0FgvK8/edit?usp=sharing',
    '2023.2/tutorials/longitudinal/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vT-GQAKqsQx-ZLwWt4DJ6_VIqHtAtVEj3LWmYzXRki8NE_ElVvsge3vz3qNq03i-vJPp6bybuDo6z42/pub?gid=1303657428&single=true&output=tsv',

    ## PD Mice
    '2023.2/tutorials/pd-mice/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1TmrdCamol0QnSeS8RdHkTVMHq4XR5f218wxreOLY2V0/edit?usp=sharing',
    '2023.2/tutorials/pd-mice/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vS-8u08T5G9MKBGBGQ2RvUZ0v17MDk9XDVqQKCnnTa2xd5-yWTANdHifVY9ZJEzRpJs9g6M8-ghhbp5/pub?gid=1509704122&single=true&output=tsv',
}
