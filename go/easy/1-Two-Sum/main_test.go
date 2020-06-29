package main

import "testing"

func TestShortInput(t *testing.T) {
	input := []int{1, 2, 3}
	target := 9
	got := twoSum(input, target)
	want := []int{1, 2}
	if len(got) != 2 {
		t.Fatal("unexpected result: twoSum did not return a slice of 2")
	}
	for i := range want {
		if got[i] != want[i] {
			t.Errorf("unexpected result: got: %v, want %v", got, want)
		}
	}
}

func TestMediumInput(t *testing.T) {
	input := []int{2, 7, 11, 15}
	target := 9
	got := twoSum(input, target)
	want := []int{0, 1}
	if len(got) != 2 {
		t.Fatal("unexpected result: twoSum did not return a slice of 2")
	}
	for i := range want {
		if got[i] != want[i] {
			t.Errorf("unexpected result: got: %v, want %v", got, want)
		}
	}
}

func TestLongInput(t *testing.T) {
	input := []int{2, 7, 11, 15, 9, 1, 8, 32, 4}
	target := 8
	got := twoSum(input, target)
	want := []int{1, 5}
	if len(got) != 2 {
		t.Fatal("unexpected result: twoSum did not return a slice of 2")
	}
	for i := range want {
		if got[i] != want[i] {
			t.Errorf("unexpected result: got: %v, want %v", got, want)
		}
	}
}
