from miniflow.utils import *
import pytest


def test_simple_addition():
	x, y = Input(), Input()
	feed_dict = {x: 10, y: 15}
	f = Add(x, y)
	result = run(f, feed_dict)
	print(result)


def test_multiple_addition():
	x, y, z = Input(), Input(), Input()
	feed_dict = {x: 10, y: 15, z: 123}
	f = Add(x, y, z)
	result = run(f, feed_dict)
	print(result)


def test_simple_multiplication():
	x, y, z = Input(), Input(), Input()
	feed_dict = {x: 10, y: 12, z: 12}
	f = Mul(x, y, z)
	result = run(f, feed_dict)
	print(result)
