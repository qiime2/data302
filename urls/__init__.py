# ----------------------------------------------------------------------------
# Copyright (c) 2016-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# flake8: noqa

from ._classifiers import MAP_CLASSIFIERS
from ._old import MAP_OLD
from ._permanent import MAP_PERMANENT
from ._usage import MAP_USAGE
from ._2019 import MAP_2019
from ._2020 import MAP_2020
from ._2021 import MAP_2021
from ._2022 import MAP_2022
from ._2023 import MAP_2023
from ._2024 import MAP_2024
from ._2025 import MAP_2025


MAP = {
    **MAP_CLASSIFIERS,

    **MAP_OLD,

    **MAP_PERMANENT,

    **MAP_USAGE,

    **MAP_2019,

    **MAP_2020,

    **MAP_2021,

    **MAP_2022,

    **MAP_2023,

    **MAP_2024,

    **MAP_2025
}


__all__ = ['MAP']
