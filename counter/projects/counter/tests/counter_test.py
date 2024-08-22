from collections.abc import Generator

import pytest
from algopy import UInt64
from algopy_testing import AlgopyTestContext, algopy_testing_context

from smart_contracts.counter.contract import Counter


@pytest.fixture()
def context() -> Generator[AlgopyTestContext, None, None]:
    with algopy_testing_context() as ctx:
        yield ctx
        ctx.reset()


def test_add(context: AlgopyTestContext) -> None:
    # Arrange
    # dummy_input = context.any_string()
    contract = Counter()

    # Act and assert
    output_add = contract.add(UInt64(7), UInt64(8))
    assert output_add == 15

    output_sub = contract.sub(UInt64(10), UInt64(8))
    assert output_sub == 2
