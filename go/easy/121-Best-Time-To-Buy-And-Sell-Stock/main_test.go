package main

import "testing"

func TestBasic(t *testing.T) {
	input := []int{10, 7, 5, 8, 11, 9}
	got := getMaxProfit(input)
	want := 6

	if got != want {
		t.Errorf("unexpected result - want: %v, got: %v", want, got)
	}

}

func TestAdvanced(t *testing.T) {
	input := []int{10, 7, 11, 8, 5, 9}
	got := getMaxProfit(input)
	want := 4

	if got != want {
		t.Errorf("unexpected result - want: %v, got: %v", want, got)
	}

}

func TestDecending(t *testing.T) {
	input := []int{10, 9, 8, 7, 6, 5}
	got := getMaxProfit(input)
	want := 0

	if got != want {
		t.Errorf("unexpected result - want: %v, got: %v", want, got)
	}

}

func TestLarge(t *testing.T) {
	input := []int{15, 6, 14, 5, 8, 11, 9}
	got := getMaxProfit(input)
	want := 8

	if got != want {
		t.Errorf("unexpected result - want: %v, got: %v", want, got)
	}

}

func TestSame(t *testing.T) {
	input := []int{10, 10, 10, 10, 10, 10}
	got := getMaxProfit(input)
	want := 0

	if got != want {
		t.Errorf("unexpected result - want: %v, got: %v", want, got)
	}

}
