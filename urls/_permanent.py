# ----------------------------------------------------------------------------
# Copyright (c) 2016-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

MAP_PERMANENT = {
    # latest env files

    # amplicon: osx
    'distro/amplicon/qiime2-amplicon-macos-latest-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/latest/passed/qiime2-amplicon-macos-latest-conda.yml',
    # amplicon: linux
    'distro/amplicon/qiime2-amplicon-ubuntu-latest-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/latest/passed/qiime2-amplicon-ubuntu-latest-conda.yml',

    # shotgun: osx
    'distro/shotgun/qiime2-shotgun-macos-latest-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/latest/passed/qiime2-shotgun-macos-latest-conda.yml',
    # shotgun: linux
    'distro/shotgun/qiime2-shotgun-ubuntu-latest-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/latest/passed/qiime2-shotgun-ubuntu-latest-conda.yml',

    # tiny: osx
    'distro/tiny/qiime2-tiny-macos-latest-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/latest/passed/qiime2-tiny-macos-latest-conda.yml',
    # tiny: linux
    'distro/tiny/qiime2-tiny-ubuntu-latest-conda.yml':
        'https://raw.githubusercontent.com/qiime2/distributions/dev/latest/passed/qiime2-tiny-ubuntu-latest-conda.yml',


    # AWS AMIs
    'distro/core/aws-amis.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/aws-amis.txt',
    'distro/core/virtualbox-images.txt':
        'https://s3-us-west-2.amazonaws.com/qiime2-data/distro/core/virtualbox-images.txt',

    # Link Shortening
    'a_diversity_metrics':
        'http://scikit-bio.org/docs/latest/generated/skbio.diversity.alpha',
}
