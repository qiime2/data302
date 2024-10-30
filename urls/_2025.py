# ----------------------------------------------------------------------------
# Copyright (c) 2016-2025, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

MAP_2025 = {
    # NOTE: UPDATE PYTHON VERSION IF WE BUMP TO 3.11
    # 2025.4 DISTROS
    # Amplicon
    'distro/amplicon/qiime2-amplicon-2025.4-py310-osx-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/2025.4/amplicon/released/qiime2-amplicon-macos-latest-conda.yml',
    'distro/amplicon/qiime2-amplicon-2025.4-py310-linux-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/2025.4/amplicon/released/qiime2-amplicon-ubuntu-latest-conda.yml',
    # Metagenome
    'distro/metagenome/qiime2-metagenome-2025.4-py310-osx-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/2025.4/metagenome/released/qiime2-metagenome-macos-latest-conda.yml',
    'distro/metagenome/qiime2-metagenome-2025.4-py310-linux-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/2025.4/metagenome/released/qiime2-metagenome-ubuntu-latest-conda.yml',
    # Pathogenome
    'distro/pathogenome/qiime2-pathogenome-2025.4-py310-osx-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/2025.4/pathogenome/released/qiime2-pathogenome-macos-latest-conda.yml',
    'distro/pathogenome/qiime2-pathogenome-2025.4-py310-linux-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/2025.4/pathogenome/released/qiime2-pathogenome-ubuntu-latest-conda.yml',
    # Tiny
    'distro/tiny/qiime2-tiny-2025.4-py310-osx-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/2025.4/tiny/released/qiime2-tiny-macos-latest-conda.yml',
    'distro/tiny/qiime2-tiny-2025.4-py310-linux-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/2025.4/tiny/released/qiime2-tiny-ubuntu-latest-conda.yml',

    # 2025.4

    '2025.4/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/atacama-soils/10p/barcodes.fastq.gz',
    '2025.4/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/atacama-soils/10p/forward.fastq.gz',
    '2025.4/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/atacama-soils/10p/reverse.fastq.gz',
    '2025.4/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/atacama-soils/1p/barcodes.fastq.gz',
    '2025.4/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/atacama-soils/1p/forward.fastq.gz',
    '2025.4/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/atacama-soils/1p/reverse.fastq.gz',
    '2025.4/tutorials/chimera/atacama-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/chimera/atacama-table.qza',
    '2025.4/tutorials/chimera/atacama-rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/chimera/atacama-rep-seqs.qza',
    '2025.4/tutorials/exporting/feature-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/exporting/feature-table.qza',
    '2025.4/tutorials/exporting/unrooted-tree.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/exporting/unrooted-tree.qza',
    '2025.4/tutorials/filtering/distance-matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/filtering/distance-matrix.qza',
    '2025.4/tutorials/filtering/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/filtering/table.qza',
    '2025.4/tutorials/filtering/taxonomy.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/filtering/taxonomy.qza',
    '2025.4/tutorials/filtering/sequences.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/filtering/sequences.qza',
    '2025.4/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2025.4/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2025.4/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2025.4/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2025.4/tutorials/fmt-cdiff-khanna/manifest.csv':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/fmt-cdiff-khanna/manifest.csv',
    '2025.4/tutorials/fmt-cdiff-khanna/sequence_files.zip':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/fmt-cdiff-khanna/sequence_files.zip',
    '2025.4/tutorials/gneiss/sample-metadata.tsv':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/gneiss/sample-metadata.tsv',
    '2025.4/tutorials/gneiss/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/gneiss/table.qza',
    '2025.4/tutorials/gneiss/taxa.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/gneiss/taxa.qza',
    '2025.4/tutorials/importing/aligned-sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/aligned-sequences.fna',
    '2025.4/tutorials/importing/casava-18-paired-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/casava-18-paired-end-demultiplexed.zip',
    '2025.4/tutorials/importing/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/casava-18-single-end-demultiplexed.zip',
    '2025.4/tutorials/importing/feature-table-v100.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/feature-table-v100.biom',
    '2025.4/tutorials/importing/feature-table-v210.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/feature-table-v210.biom',
    '2025.4/tutorials/importing/muxed-se-barcode-in-seq.fastq.gz':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/importing/muxed-se-barcode-in-seq.fastq.gz',
    '2025.4/tutorials/importing/pe-64-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/pe-64-manifest',
    '2025.4/tutorials/importing/pe-64.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/pe-64.zip',
    '2025.4/tutorials/importing/se-33-manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/se-33-manifest',
    '2025.4/tutorials/importing/se-33.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/se-33.zip',
    '2025.4/tutorials/importing/sequences.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/sequences.fna',
    '2025.4/tutorials/importing/unrooted-tree.tre':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/unrooted-tree.tre',
    '2025.4/tutorials/importing/muxed-pe-barcode-in-seq/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/muxed-pe-barcode-in-seq/forward.fastq.gz',
    '2025.4/tutorials/importing/muxed-pe-barcode-in-seq/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/importing/muxed-pe-barcode-in-seq/reverse.fastq.gz',
    '2025.4/tutorials/longitudinal/ecam_table_taxa.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/longitudinal/ecam_table_taxa.qza',
    '2025.4/tutorials/longitudinal/ecam_shannon.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/longitudinal/ecam_shannon.qza',
    '2025.4/tutorials/longitudinal/unweighted_unifrac_distance_matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/longitudinal/unweighted_unifrac_distance_matrix.qza',
    '2025.4/tutorials/longitudinal/ecam_table_maturity.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/longitudinal/ecam_table_maturity.qza',
    '2025.4/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz',
    '2025.4/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz',
    '2025.4/tutorials/metadata/faith_pd_vector.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/metadata/faith_pd_vector.qza',
    '2025.4/tutorials/metadata/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/metadata/rep-seqs.qza',
    '2025.4/tutorials/metadata/taxonomy.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/metadata/taxonomy.qza',
    '2025.4/tutorials/metadata/unweighted_unifrac_pcoa_results.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/metadata/unweighted_unifrac_pcoa_results.qza',
    '2025.4/tutorials/otu-clustering/seqs.fna':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/otu-clustering/seqs.fna',
    '2025.4/tutorials/otu-clustering/85_otus.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/otu-clustering/85_otus.qza',
    '2025.4/tutorials/pd-mice/animal_distal_gut.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/pd-mice/animal_distal_gut.qza',
    '2025.4/tutorials/pd-mice/demultiplexed_seqs.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/pd-mice/demultiplexed_seqs.zip',
    '2025.4/tutorials/pd-mice/manifest':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/pd-mice/manifest',
    '2025.4/tutorials/pd-mice/ref_seqs_v4.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/pd-mice/ref_seqs_v4.qza',
    '2025.4/tutorials/pd-mice/ref_tax.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/pd-mice/ref_tax.qza',
    '2025.4/tutorials/quality-control/qc-mock-3-expected.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/quality-control/qc-mock-3-expected.qza',
    '2025.4/tutorials/quality-control/qc-mock-3-observed.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/quality-control/qc-mock-3-observed.qza',
    '2025.4/tutorials/quality-control/query-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/quality-control/query-seqs.qza',
    '2025.4/tutorials/quality-control/reference-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/quality-control/reference-seqs.qza',
    '2025.4/tutorials/quality-control/query-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/quality-control/query-table.qza',
    '2025.4/tutorials/read-joining/atacama-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/read-joining/atacama-seqs.qza',
    '2025.4/tutorials/read-joining/fj-joined.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/read-joining/fj-joined.zip',
    '2025.4/tutorials/sample-classifier/atacama-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/sample-classifier/atacama-table.qza',
    '2025.4/tutorials/sample-classifier/moving-pictures-table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/sample-classifier/moving-pictures-table.qza',
    '2025.4/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2025.4/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/training-feature-classifiers/85_otus.fasta',
    '2025.4/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2025.4/tutorials/training-feature-classifiers/rep-seqs.qza',
    '2025.4/tutorials/phylogeny/rep-seqs.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/phylogeny/rep-seqs.qza',
    '2025.4/tutorials/utilities/faith-pd-vector.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/utilities/faith-pd-vector.qza',
    '2025.4/tutorials/utilities/jaccard-pcoa.qza':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/utilities/jaccard-pcoa.qza',
    '2025.4/tutorials/utilities/taxa-barplot.qzv':
        'https://qiime2-data.s3-us-west-2.amazonaws.com/2025.4/tutorials/utilities/taxa-barplot.qzv',
    '2025.4/tutorials/liao/fmt-metadata.tsv':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2025.4/tutorials/liao/fmt-metadata.tsv',
    '2025.4/tutorials/liao/sample-metadata.tsv':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2025.4/tutorials/liao/sample-metadata.tsv',
    '2025.4/tutorials/liao/transplant-metadata.tsv':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2025.4/tutorials/liao/transplant-metadata.tsv',
    '2025.4/tutorials/liao/rep-seqs.qza':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2025.4/tutorials/liao/rep-seqs.qza',
    '2025.4/tutorials/liao/full-feature-table.qza':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2025.4/tutorials/liao/full-feature-table.qza',
    '2025.4/tutorials/liao/fastq-casava.zip':
        'https://qiime2-data.s3.us-west-2.amazonaws.com/2025.4/tutorials/liao/fastq-casava.zip',

    # Sample Metadata (hosted on Google Sheets)
    ## All of the following tutorials use the *new* docs sharing menu, via "File -> Publish to the Web" dialog for TSV export.

    ## FMT
    '2025.4/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1UfHnTvsojIRozNlFLtKW-KBX7QIiKBf18jkaonjGjbE/edit?usp=sharing',
    '2025.4/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vQKaiB4AEby0RdTftP8f1ilOSPhFf66X16CNRgyT4Z0rbSk4Epy4CC5BcUekjhCnr05haSbWxeGZf1P/pub?gid=0&single=true&output=tsv',

    ## Moving Pictures
    '2025.4/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/13OLfRy4bt3IiLdHXHkkfdMxaJXJ65mEjAxe1A01frBQ/edit?usp=sharing',
    '2025.4/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vSETdFG23WYy3u0MhEQRlw1gE2oQrAlPW2LKfETMXbdF4wH9ZXkpOau4cRWwTqm6vwap0ns8Pu5B8wN/pub?gid=0&single=true&output=tsv',

    ## Atacama
    '2025.4/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1eQSLklA2OR1Vo0bS6EHz1Qq9NIuIa1ANhfn7Qek2dwg/edit?usp=sharing',
    '2025.4/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vQiT_TuZ-g2JC790DXFP9Fhkhti_vjNvJoqDzRscGoculfLBYl2VTAYkAOoHVhnYCLe86-xNnXU84tQ/pub?gid=0&single=true&output=tsv',

    ## Longitudinal
    '2025.4/tutorials/longitudinal/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1EZVm7gfw0fzz4RNkx1TPiJjhpPLWE6VcAIpAB_JDhcg/edit?usp=sharing',
    '2025.4/tutorials/longitudinal/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vRJL3EmUTIIVqW_HU0eXFiOVIZ-n0S36mFLRHqpRZrFANsBC5Duga_DiGpxuRU1C-aq0gBL28zhDIY3/pub?gid=1303657428&single=true&output=tsv',

    ## PD Mice
    '2025.4/tutorials/pd-mice/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1KW00pThfZy5Kce7L2tqnuN11dwqzMWec5G6_jTfT2JE/edit?usp=sharing',
    '2025.4/tutorials/pd-mice/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vSYXZbF5LZGfXvrWLVGfT5u3zj23fiAIsGDJd_DRzF0bTBBRmeQxjIBUdMruztI2M_HWP4STM4rDoH0/pub?gid=1509704122&single=true&output=tsv',
}
