# ----------------------------------------------------------------------------
# Copyright (c) 2016-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

MAP_CLASSIFIERS = {
    ## sklearn 0.21.2

    # SEPP reference databases
    'classifiers/sepp-ref-dbs/sepp-refs-gg-13-8.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sepp-ref-dbs/sepp-refs-gg-13-8.qza',
    'classifiers/sepp-ref-dbs/sepp-refs-silva-128.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sepp-ref-dbs/sepp-refs-silva-128.qza',

    ## sklearn 0.24.1

    # Greengenes
    'classifiers/greengenes/gg_12_10_otus.tar.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/greengenes/gg_12_10_otus.tar.gz',
    'classifiers/greengenes/gg_13_5_otus.tar.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/greengenes/gg_13_5_otus.tar.gz',
    'classifiers/greengenes/gg_13_8_otus.tar.gz':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/greengenes/gg_13_8_otus.tar.gz',
    'classifiers/greengenes/gg_2022_10_backbone_full_length.nb.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/greengenes/gg_2022_10_backbone_full_length.nb.qza',
    'classifiers/greengenes/gg_2022_10_backbone.v4.nb.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/greengenes/gg_2022_10_backbone.v4.nb.qza',

    ## sklearn 1.4.2

    # Greengenes
    'classifiers/sklearn-1.4.2/greengenes/gg-13-8-99-515-806-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/greengenes/gg-13-8-99-515-806-nb-classifier.qza',

    # Greengenes 2
        # 2022.10
    'classifiers/sklearn-1.4.2/greengenes2/2022.10.backbone.full-length.nb.sklearn-1.4.2.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/greengenes2/2022.10.backbone.full-length.nb.sklearn-1.4.2.qza',
    'classifiers/sklearn-1.4.2/greengenes2/2022.10.backbone.v4.nb.sklearn-1.4.2.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/greengenes2/2022.10.backbone.v4.nb.sklearn-1.4.2.qza',
        # 2024.9
    'classifiers/sklearn-1.4.2/greengenes2/2024.09.backbone.full-length.nb.sklearn-1.4.2.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/greengenes2/2024.09.backbone.full-length.nb.sklearn-1.4.2.qza',
    'classifiers/sklearn-1.4.2/greengenes2/2024.09.backbone.v4.nb.sklearn-1.4.2.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/greengenes2/2024.09.backbone.v4.nb.sklearn-1.4.2.qza',

    # GTDB
    'classifiers/sklearn-1.4.2/gtdb/gtdb_classifier_r220.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/gtdb/gtdb_classifier_r220.qza',
    'classifiers/sklearn-1.4.2/gtdb/gtdb_human_stool_weighted_classifier_r220.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/gtdb/gtdb_human_stool_weighted_classifier_r220.qza',
    'classifiers/sklearn-1.4.2/gtdb/gtdb_diverse_weighted_classifier_r220.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/gtdb/gtdb_diverse_weighted_classifier_r220.qza',

    # Silva
    'classifiers/sklearn-1.4.2/silva/silva-138-99-nb-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/silva/silva-138-99-nb-classifier.qza',
    'classifiers/sklearn-1.4.2/silva/silva-138-99-nb-human-stool-weighted-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/silva/silva-138-99-nb-human-stool-weighted-classifier.qza',
    'classifiers/sklearn-1.4.2/silva/silva-138-99-nb-diverse-weighted-classifier.qza':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/classifiers/sklearn-1.4.2/silva/silva-138-99-nb-diverse-weighted-classifier.qza',
}
