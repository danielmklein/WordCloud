'''
Test Cases for AnalysisEngine Class for WordCloud Project

Daniel Klein
Computer-Based Honors Program
The University of Alabama
9.27.2013
'''

import unittest
import os, os.path
from AnalysisEngine import AnalysisEngine
from Document import Document
from SupremeCourtOpinionMetadata import SupremeCourtOpinionMetadata

'''
Yep. Holes. 
'''

TEXT1 = \
"""\
There is no lake at Camp Green Lake. There once was a very large lake here, the \
largest lake in Texas. That was over a hundred years ago. Now it is just a dry, \
flat wasteland. \
There used to be a town of Green Lake as well. The town shriveled and dried up \
along with the lake, and the people who lived there. \
During the summer the daytime temperature hovers around ninety-five degrees in \
the shade -- if you can find any shade. There's not much shade in a big dry \
lake. \
The only trees are two old oaks on the eastern edge of the "lake." A hammock is \
stretched between two trees, and a log cabin stands behind that. \
The campers are forbidden to lie in the hammock. It belongs to the Warden. The \
Warden owns the shade. \
Out on the lake, rattlesnakes and scorpions find shade under rocks and in the \
holes dug by the campers. \
Here's a good rule to remember about rattlesnakes and scorpions: If you don't \
bother them, they won't bother you. Usually. \
Being bitten by a scorpion or even a rattlesnake is not the worst thing that \
can happen to you. You won't die. Usually. \
Sometimes a camper will try to be bitten by a scorpion, or even a small \
rattlesnake. Then he will get to spend a day or two recovering in his tent, \
instead of having to dig a hole out on the lake. \
But you don't want to be bitten by a yellow-spotted lizard. That's the worst \
thing that can happen to you. You will die a slow and painful death. Always. \
If you get bitten by a yellow-spotted lizard, you might as well go into the \
shade of the oak trees and lie in the hammock. \
There is nothing anyone can do to you anymore.\
"""

TEXT2 = \
"""\
The reader is probably asking: Why would anyone go to Camp Green Lake? \
Most campers weren't given a choice. Camp Green Lake is a camp for bad boys. \
If you take a bad boy and make him dig a hole every day in the hot sun, it \
will turn him into a good boy. That was what some people thought. \
Stanley Yelnats was given a choice. The judge said, "You may go to jail, or \
you may go to Camp Green Lake." \
Stanley was from a poor family. He had never been to camp before.\
"""

TEXT3 = \
"""\
Stanley Yelnats was the only passenger on the bus, not counting the driver \
or the guard. The guard sat next to the driver with his seat turned around \
facing Stanley. A rifle lay across his lap. \
Stanley was sitting about ten rows back, handcuffed to his armrest. His \
backpack lay on the seat next to him. It contained his toothbrush, toothpaste \
and a box of stationery his mother had given him. He'd promised to write her \
at least once a week. \
He looked out the window, although there wasn't much to see -- mostly fields \
of hay and cotton. He was on a long bus ride to nowhere. The bus wasn't air-\
conditioned, and the hot, heavy air was almost as stifling as the handcuffs. \
Stanley and his parents had tried to pretend that he was just going away to \
camp for a while, just like rich kids do. When Stanley was younger he used to \
play with stuffed animal, and pretend the animals were at camp. Camp Fun and \
Games he called it. Sometimes he'd have them play soccer with a marble. Other \
times they'd run an obstacle course, or go bungee jumping off a table, tied \
to broken rubber bands. Now Stanley tried to pretend he was going to Camp Fun \
and Games. Maybe he'd make some friends, he thought. At least he'd get to \
swim in the lake.
"""

TEXT4 = \
"""\
He didn't have any friends at home. He was overweight and the kids at his \
middle school often teased him about his size. Even his teachers sometimes \
made cruel comments without realizing it. On his last day of school, his math \
teacher, Mrs. Bell, taught ratios. As an example, she chose the heaviest kid \
in the class and the lightest kid in the class, and had them weigh themselves. \
Stanley weighed three times as much as the other boy. Mrs. Bell wrote the \
ratio on the board, 3:1, unaware of how much embarrassment she had caused \
both of them. \
Stanley was arrested later that day. \
He looked at the guard who sat slumped in his seat and wondered if he had \
fallen asleep. The guard was wearing sunglasses, so Stanley couldn't see his \
eyes. \
Stanley was not a bad kid. He was innocent of the crimes for which he was \
convicted. He'd just been in the wrong place at the wrong time. It was all \
because of his no-good-dirty-rotten-pig-stealing-greate-great-grandfather! \
He smiled. It was a family joke. Whenever anything went wrong, they always \
blamed Stanley's no-good-dirty-rotten-pig-stealing-great-great-grandfather. \\
"""

TEXT5 = \
"""\
Supposedly, he had a great-great-grandfather who had stolen a pig from a one-\
legged Gypsy, and she put a curse on him and all his descendants. Stanley and \
his parents didn't believe in curses, of course, but whenever anything went \
wrong, it felt good to be able to blame someone. \
Things went wrong a lot. They always seemed to be in the wrong place at the \
wrong time. \
He looked out the window at the vast emptiness. He watched the rise and fall \
of a telephone wire. In his mind he could hear his father's gruff voice \
softly sing to him. \
"If only, if only," the woodpecker sighs, "The bark on the tree was just a \
little bit softer." While the wolf waits below, hungry and lonely, He cries \
to the moon, "If only, if only." \
If was a song his father used to sing to him. The melody was sweet and sad, \
but Stanley's favorite part was when his father would howl the world "moon." \
The bus hit a small bump and the guard sat up, instantly alert.\
"""

CURRENT_PATH = os.path.abspath(os.curdir)


def build_subsets():
    blank_metadata = SupremeCourtOpinionMetadata()
    
    doc1_output = os.path.join(CURRENT_PATH, "doc1_output")
    doc1 = Document(blank_metadata, TEXT1, doc1_output)
    
    doc2_output = os.path.join(CURRENT_PATH, "doc2_output")
    doc2 = Document(blank_metadata, TEXT2, doc2_output)
    
    doc3_output = os.path.join(CURRENT_PATH, "doc3_output")
    doc3 = Document(blank_metadata, TEXT3, doc3_output)
    
    doc4_output = os.path.join(CURRENT_PATH, "doc4_output")
    doc4 = Document(blank_metadata, TEXT4, doc4_output)

    doc5_output = os.path.join(CURRENT_PATH, "doc5_output")
    doc5 = Document(blank_metadata, TEXT5, doc5_output)
    subsets = [[doc1], [doc2], [doc3, doc4, doc5]]
    return subsets


class AnalysisEngineTest(unittest.TestCase):


    def setUp(self):
        self.subsets = build_subsets()
        self.test_engine = AnalysisEngine([])


    def tearDown(self):
        del self.subsets
        del self.test_engine


    def testAnalyzeWithSingleSubset(self):
        print "Testing AnalysisEngine.analyze_docs() with single subset..."
        self.test_engine.set_subsets([self.subsets[2]])
        print self.test_engine.subsets
        ##
        self.test_engine.analyze_docs()
        ##
        self.fail("haven't written this test yet")
        print "Finished testing AnalysisEngine.analyze_docs()..."
        
    
    def testAnalyzeWithMultipleSubsets(self):
        print "Testing AnalysisEngine.analyze_docs() with multiple subsets..."
        self.test_engine.set_subsets(self.subsets)
        print self.test_engine.subsets
        ##
        self.test_engine.analyze_docs()
        ##
        self.fail("haven't written this test yet")
        print "Finished testing AnalysisEngine.analyze_docs()..."
    
    def testAnalyzeWithZeroSubsets(self):
        print "Testing AnalysisEngine.analyze_docs() with zero subsets..."
        self.test_engine.set_subsets([])
        print self.test_engine.subsets
        ##
        self.test_engine.analyze_docs()
        ##
        self.fail("haven't written this test yet")
        print "Finished testing AnalysisEngine.analyze_docs()..."
    
    
    def testAnalysisWithInvalidInput(self):
        print "Testing AnalysisEngine.analyze_docs() with invalid input..."
        self.subsets.append(["not a doc", "nor is this"])
        self.assertRaises(Exception, self.test_engine.set_subsets, self.subsets)
        print self.test_engine.subsets
        self.fail("haven't written this test yet")
        print "Finished testing AnalysisEngine.analyze_docs()..."
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()