#!/usr/bin/perl -w
use strict;

my $usage = "$0 [\"Species name\" / infile.txt]\n";

my $taxdir = "/hosts/linuxhome/embryo/dutilh2/tax_20150123";
#$taxdir = "/home/dutilh";

# check number of arguments
if (scalar @ARGV != 1) {
	die $usage; }

my @input = ();
if (open (IN, "<$ARGV[0]")) {
	while (my $l = <IN>) {
		chomp ($l);
		push (@input, $l); }
	close (IN); }
else {
	push (@input, $ARGV[0]); }

# read node parents from taxonomy nodes file
print STDERR "Reading file $taxdir/nodes.dmp";
open (NODES, "<$taxdir/nodes.dmp") or die "Can't open $taxdir/nodes.dmp: $!\n";
my %parent = ();
my %level = ();
while (my $l = <NODES>) {
	my @a = split /\t/o, $l;
	$parent{$a[0]} = $a[2];
	$level{$a[0]} = $a[4]; }
close (NODES);
print STDERR " - done\n";

# read scientific names from taxonomy names file
print STDERR "Reading file $taxdir/names.dmp";
open (NAMES, "<$taxdir/names.dmp") or die "Can't open $taxdir/names.dmp: $!\n";
my %names = ();
my %levels = ();
my %index = ();
while (my $l = <NAMES>) {
        my @a = split /\t/o, $l;
	++$index{$a[2]}{$a[0]};
	my $lc = lc ($a[2]);
	$lc =~ s/\W+/_/g;
	$lc =~ s/^_+//;
	$lc =~ s/_+\Z//;
	++$index{$lc}{$a[0]};
	if ($a[6] eq "scientific name") {
        	$names{$a[0]} = $a[2]; } }
close (NAMES);
print STDERR " - done\n";

# go through names and find tax ID
while (my $this = splice (@input, 0, 1)) {
	my $lineage = &lineage ($this);
	print "$this\t$lineage\t$level{$this}\t$names{$this}\n"; }

# get taxonomic lineage until root
sub lineage {
	my $node = $_[0];
	my $lineage = $node;
	if ($node == 0) {
		return (0); }
	while ($node != 1) {
		$node = $parent{$node};
		$lineage .= ",$node"; }
	return ($lineage); }

