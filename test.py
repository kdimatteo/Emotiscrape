#!/usr/bin/python

import emotiscrape

if __name__ == "__main__":

	emo = emotiscrape.Emotiscrape()
	print "---------\nTEST MODE\n---------"
	test_samples = [
        ("pos", "i love you harry!"),
        ("neg", "This is incredibly annoying, i hate working here and i hate this crummy application"),
        ("neg", "You are a terrible person and everything you do is bad."),
        ("pos", "I love you all and you make me happy"),
        ("neg", "I frown whenever I see you in a poor state of mind"),
        ("pos", "Finally getting rich from my ideas. They make me smile"),
        ("neg", "My mommy is poor"),
        ("pos", "I love butterflies. Yay for happy"),
        ("neg", "Everything is fail today and I hate stuff"),
        ("pos", "Larry is my friend, but boy is he shady")
    ]
    
	for expected_result, sample in test_samples:
		o = emo.analyze_string(sample)
		if o.get("classification") == expected_result:
			status = "\033[92m%s\033[0m" % "pass"
		else:
			status = "\033[91m%s\033[0m" % "fail"

		print "[%s] %s : %s \t\t %s" % (status, o.get("classification"), o.get("probability_delta")*100, o.get("original_text"))
