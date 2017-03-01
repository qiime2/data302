# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

MAP = {
    # DISTRO
    'distro/core/2.0.6':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime206-1484941248.zip',
    'distro/core/qiime206.zip':  # LEGACY, we can probably delete this
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime206-1484941248.zip',
    'distro/core/2017.2':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime20172-1486602522.zip',
    'distro/core/qiime20172-1486602522.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime20172-1486602522.zip',
    'distro/core/qiime206-1479486933.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime206-1479486933.zip',
    'distro/core/qiime206-1484941248.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime206-1484941248.zip',
    'distro/core/qiime2-2017.2-conda-osx-64.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime2-2017.2-conda-osx-64.txt',
    'distro/core/qiime2-2017.2-conda-linux-64.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/qiime2-2017.2-conda-linux-64.txt',

    # 2.0.5
    '2.0.5/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2.0.5/tutorials/88soils/88soils-tutorial-demux-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/88soils/88soils-tutorial-demux-10p.qza',
    '2.0.5/tutorials/88soils/88soils-tutorial-demux-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/88soils/88soils-tutorial-demux-1p.qza',
    '2.0.5/tutorials/88soils/88soils-tutorial-demux-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/88soils/88soils-tutorial-demux-full.qza',
    '2.0.5/tutorials/88soils/88soils-tutorial-raw-sequences.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/88soils/88soils-tutorial-raw-sequences.qza',
    '2.0.5/tutorials/examples/feature-table.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/examples/feature-table.biom',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-1-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-1-full.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-demux-2-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-demux-2-full.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza',
    '2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza',
    '2.0.5/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz',
    '2.0.5/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.5/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz',

    # 2.0.6
    '2.0.6/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2.0.6/common/gg-13-8-99-full-length-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/common/gg-13-8-99-full-length-nb-classifier.qza',
    '2.0.6/common/silva-119-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/common/silva-119-99-515-806-nb-classifier.qza',
    '2.0.6/common/silva-119-99-full-length-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/common/silva-119-99-full-length-nb-classifier.qza',
    '2.0.6/tutorials/88soils/88soils-tutorial-demux-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/88soils/88soils-tutorial-demux-10p.qza',
    '2.0.6/tutorials/88soils/88soils-tutorial-demux-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/88soils/88soils-tutorial-demux-1p.qza',
    '2.0.6/tutorials/88soils/88soils-tutorial-demux-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/88soils/88soils-tutorial-demux-full.qza',
    '2.0.6/tutorials/88soils/88soils-tutorial-raw-sequences.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/88soils/88soils-tutorial-raw-sequences.qza',
    '2.0.6/tutorials/examples/feature-table.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/examples/feature-table.biom',
    '2.0.6/tutorials/filtering-feature-tables/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/filtering-feature-tables/table.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-1-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-1-full.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-demux-2-full.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-demux-2-full.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-1.qza',
    '2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/fmt/fmt-tutorial-raw-sequences-2.qza',
    '2.0.6/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip',
    '2.0.6/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/moving-pictures/raw-sequences/barcodes.fastq.gz',
    '2.0.6/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/moving-pictures/raw-sequences/sequences.fastq.gz',
    '2.0.6/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2.0.6/tutorials/training-feature-classifiers/aligned_85_otu_sequences.fasta.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/training-feature-classifiers/aligned_85_otu_sequences.fasta.gz',
    '2.0.6/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2.0.6/tutorials/training-feature-classifiers/rep-seqs.qza',

    # 2017.2
    '2017.2/common/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/common/gg-13-8-99-515-806-nb-classifier.qza',
    '2017.2/common/gg-13-8-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/common/gg-13-8-99-nb-classifier.qza',
    '2017.2/common/silva-119-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/common/silva-119-99-515-806-nb-classifier.qza',
    '2017.2/common/silva-119-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/common/silva-119-99-nb-classifier.qza',
    '2017.2/tutorials/atacama-soils/10p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/10p/barcodes.fastq.gz',
    '2017.2/tutorials/atacama-soils/10p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/10p/forward.fastq.gz',
    '2017.2/tutorials/atacama-soils/10p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/10p/reverse.fastq.gz',
    '2017.2/tutorials/atacama-soils/1p/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/1p/barcodes.fastq.gz',
    '2017.2/tutorials/atacama-soils/1p/forward.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/1p/forward.fastq.gz',
    '2017.2/tutorials/atacama-soils/1p/reverse.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/atacama-soils/1p/reverse.fastq.gz',
    '2017.2/tutorials/filtering/distance-matrix.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/filtering/distance-matrix.qza',
    '2017.2/tutorials/filtering/table.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/filtering/table.qza',
    '2017.2/tutorials/fmt/fmt-tutorial-demux-1-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/fmt/fmt-tutorial-demux-1-10p.qza',
    '2017.2/tutorials/fmt/fmt-tutorial-demux-1-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/fmt/fmt-tutorial-demux-1-1p.qza',
    '2017.2/tutorials/fmt/fmt-tutorial-demux-2-10p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/fmt/fmt-tutorial-demux-2-10p.qza',
    '2017.2/tutorials/fmt/fmt-tutorial-demux-2-1p.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/fmt/fmt-tutorial-demux-2-1p.qza',
    '2017.2/tutorials/importing-sequence-data/casava-18-paired-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/importing-sequence-data/casava-18-paired-end-demultiplexed.zip',
    '2017.2/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/importing-sequence-data/casava-18-single-end-demultiplexed.zip',
    '2017.2/tutorials/importing-sequence-data/feature-table-v100.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/importing-sequence-data/feature-table-v100.biom',
    '2017.2/tutorials/importing-sequence-data/feature-table-v210.biom':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/importing-sequence-data/feature-table-v210.biom',
    '2017.2/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/moving-pictures/emp-single-end-sequences/barcodes.fastq.gz',
    '2017.2/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/moving-pictures/emp-single-end-sequences/sequences.fastq.gz',
    '2017.2/tutorials/training-feature-classifiers/85_otu_taxonomy.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/training-feature-classifiers/85_otu_taxonomy.txt',
    '2017.2/tutorials/training-feature-classifiers/85_otus.fasta':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/training-feature-classifiers/85_otus.fasta',
    '2017.2/tutorials/training-feature-classifiers/rep-seqs.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/2017.2/tutorials/training-feature-classifiers/rep-seqs.qza',
    '2017.2/tutorials/atacama-soils/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1xMP1EjKZDrzdKLnQr7LGVAY35ongxrreT28k0EACtfg/export?gid=0&format=tsv',
    '2017.2/tutorials/atacama-soils/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1xMP1EjKZDrzdKLnQr7LGVAY35ongxrreT28k0EACtfg/edit?usp=sharing',
    '2017.2/tutorials/fmt/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/197f9kTKhcvcwqIjQaSkDHqsWeLO5jNN2_LlAN3NuadI/export?gid=0&format=tsv',
    '2017.2/tutorials/fmt/sample_metadata':
        'https://docs.google.com/spreadsheets/d/197f9kTKhcvcwqIjQaSkDHqsWeLO5jNN2_LlAN3NuadI/edit?usp=sharing',
    '2017.2/tutorials/moving-pictures/sample_metadata.tsv':
        'https://docs.google.com/spreadsheets/d/1WwCnhP7VbiVXY5-XHLoYAT-wAU68ItEF117TYJeQCrg/export?gid=0&format=tsv',
    '2017.2/tutorials/moving-pictures/sample_metadata':
        'https://docs.google.com/spreadsheets/d/1WwCnhP7VbiVXY5-XHLoYAT-wAU68ItEF117TYJeQCrg/edit?usp=sharing',
}
