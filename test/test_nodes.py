from miniflow.utils import *


def test_simple_addition():
	x, y = Input(), Input()
	feed_dict = {x: 10, y: 15}
	f = Add(x, y)
	result = run(f, feed_dict)
	assert 25 == result


def test_multiple_addition():
	x, y, z = Input(), Input(), Input()
	feed_dict = {x: 10, y: 15, z: 123}
	f = Add(x, y, z)
	result = run(f, feed_dict)
	assert 148 == result


def test_simple_multiplication():
	x, y, z = Input(), Input(), Input()
	feed_dict = {x: 10, y: 12, z: 12}
	f = Mul(x, y, z)
	result = run(f, feed_dict)
	assert 1440 == result


def test_mult_add():
	x, y, z = Input(), Input(), Input()
	add = Add(x, y)
	res = Mul(add, z)
	feed_dict = {x: 2, y: 3, z: 2}
	result = run(res, feed_dict)
	assert 10 == result
