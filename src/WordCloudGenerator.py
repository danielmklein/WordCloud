import random

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import numpy

FONT_PATH = "C:/Windows/Fonts/FRABK.ttf"

class WordCloudGenerator():
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    This class and its functionality are really quite simple -- given a 
    weighted list of terms (in a list of (term,weight) tuples) (and probably 
    a parameter specifying the number of terms to illustrate), this will return
    a word cloud that visualizes the most important terms and how important 
    they are relative to each other.
    
    Much inspiration for this module was drawn from:
    https://github.com/amueller/word_cloud and
    http://peekaboo-vision.blogspot.com/2012/11/a-wordcloud-in-python.html
    '''


    def __init__(self, weighted_terms, output_filename, 
                 image_height=200, image_width=400):
        '''
        Constructor
        '''
        self.weighted_terms = weighted_terms
        self.output_filename = output_filename
        self.image_height = image_height
        self.image_width = image_width

    
    def query_integral_image(self, integral_image, size_x, size_y):
        '''
        This is adapted from the word cloud GitHub project mentioned
        in the above comments.
        '''
        x = integral_image.shape[0]
        y = integral_image.shape[1]
        hits = 0
        
        # count possible locations
        for i in xrange(x - size_x):
            for j in xrange(y - size_y):
                area = integral_image[i, j] \
                    + integral_image[i + size_x, j + size_y]
                area -= integral_image[i + size_x, j] \
                    + integral_image[i, j + size_y]
                if not area:
                    hits += 1
        if not hits:
            # no room left
            return None
        # pick location at random
        goal = numpy.random.randint(hits)
        hits = 0
        for i in xrange(x - size_x):
            for j in xrange(y - size_y):
                area = integral_image[i, j] \
                    + integral_image[i + size_x, j + size_y]
                area -= integral_image[i + size_x, j] \
                    + integral_image[i, j + size_y]
                if not area:
                    hits += 1
                    if hits == goal:
                        return i,j
        
        
    def generate_word_cloud(self, num_terms_to_visualize=50, margin=5):
        # check length of term dict -- must be GT 0
        if len(self.weighted_terms) <= 0:
            print "List of terms must contain at least one term and weight."
            print "The current list contains {0} terms.".format(
                                                        self.weighted_terms)
            return 0
        
        # make sure all weights are 0 <= weight <= 1
        for term, weight in self.weighted_terms:
            if weight < 0 or 1 < weight:
                print "All weights must be between 0 and 1."
                print "Term {0} has weight {1}.".format(term, weight)
                return 0
            
        # sort term list by weights
        self.weighted_terms.sort(key=lambda pair: pair[1], reverse=True)
        # test output
        print self.weighted_terms
        # /test output
        
        # create B/W image
        black_white_image = Image.new("L", (self.image_width, self.image_height))
        # draw image
        draw = ImageDraw.Draw(black_white_image)
        # instantiate integral
        integral = numpy.zeros((self.image_height, self.image_width),
                               dtype=numpy.uint32)
        # instantiate image array
        image_array = numpy.asarray(black_white_image) 
        # set font_sizes, positions, orientations to blank lists
        font_sizes, term_positions, term_orientations = [], [], []
        
        # set font_size to "large enough" value (1000?)
        font_size = 200
        
        # for each term:weight pair:
        for term, weight in self.weighted_terms:
            font_size = min(font_size, int(100 * numpy.log(weight + 100)))
            # while True:
            while True:
                # set font
                font = ImageFont.truetype(FONT_PATH, font_size)
                # optionally rotate orientation
                orientation = random.choice([None, Image.ROTATE_90])
                # set transposed_font with new orientation
                transposed_font = ImageFont.TransposedFont(font,
                                                        orientation=orientation)
                # set font to transponsed_font
                draw.setfont(transposed_font)
                # get size of box for current term
                term_box_size = draw.textsize(term)
                # use query_integral_image to get possible places for term
                location_result = self.query_integral_image(integral, 
                                                       term_box_size[1] + margin,
                                                       term_box_size[0] + margin
                                                       )
                # if there are results or font_size hits 0:
                if location_result is not None or font_size == 0:
                    # break from while true
                    break
                # otherwise decrement font_size and loop
                else:
                    font_size -= 1
  
            # if font_size hit 0:
            if font_size == 0:
                # this means we can't draw anymore
                # break from foreach
                break
                
            # set x and y coords using result and margin value
            x, y = numpy.array(location_result) + margin // 2
            # perform the actual drawing of the term
            draw.text((y, x), term, fill="white")
            term_positions.append((x, y))
            term_orientations.append(orientation)
            font_sizes.append(font_size) 
            # recompute integral image
            image_array = numpy.asarray(black_white_image)
            
            # recompute bottom right
            partial_integral = numpy.cumsum(numpy.cumsum(image_array[x:, y:],
                                                         axis=1), axis=0)
            # paste recomputed part into old image
            if x > 0:
                if y > 0:
                    partial_integral += (integral[x-1, y:]
                                         - integral[x-1, y-1])
                else:
                    partial_integral += integral[x-1, y:]
            if y > 0:
                partial_integral += integral[x:, y-1][:, numpy.newaxis]
            integral[x:, y:] = partial_integral
        '''
        # #redraw in color
        # create new color image
        color_image = Image.new("RGB", (self.image_width, self.image_height))
        color_draw = ImageDraw.Draw(color_image)
        # build a list of big tuples with all the needed info for each term
        terms = [term for term, weight in self.weighted_terms]
        term_data = zip(terms, font_sizes, term_positions, term_orientations)
        # for each item in that list:
        for term, font_size, term_position, term_orientation in term_data:
            # set font
            font = ImageFont.truetype(FONT_PATH, font_size)
            # transpose font
            transposed_font = ImageFont.TransposedFont(font, 
                                                    orientation=term_orientation)
            # draw the text
            color_draw.setfont(transposed_font)
            color_draw.text((term_position[1], term_position[0]),
                             term, fill="hsl(%d" % random.randint(0, 255)
                             + ", 80%, 50%)")
        '''
        # display image
        black_white_image.show()
        #color_image.show()
        
        # save image to file
        #black_white_image.save(self.output_filename)
        #color_image.save(self.output_filename)


