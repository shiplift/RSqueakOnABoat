*Values-lambcompare
valuesBenchFilter

	| e f lst1 lst2 res start end gcAfter gcBefore |
	e := VVector new.
	f := VNil nil.
	lst1 := VCons withAll: (VCons alternatingArrayOfSize: self with: e andAlternate: f).
	lst2 := VCons withAll: (VCons alternatingArrayOfSize: self with: e andAlternate: f).
	Smalltalk garbageCollect.
	gcBefore := RSqueak gcTimings.
	start := Time utcMicrosecondClock.
	res := lst1 filter: [:element | element = e].
	end := Time utcMicrosecondClock.
	gcAfter := RSqueak gcTimings.
	RSqueak reportBenchStartedAt: start until: end gcBefore: gcBefore after: gcAfter.
	self assert: (res isKindOf: VNil) not.
	^ 0