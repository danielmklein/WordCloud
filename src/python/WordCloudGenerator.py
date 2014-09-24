import random
import numpy
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from src.core.python.WordCloudConstants import *


class WordCloudGenerator(object):
    '''
    Daniel Klein
    Computer-Based Honors Program
    The University of Alabama
    9.26.2013
    
    This class and its functionality are relatively simple -- given a 
    weighted list of terms (in a list of (term,weight) tuples) (and probably 
    a parameter specifying the number of terms to illustrate), this will return
    a word cloud that visualizes the most important terms and how important 
    they are relative to each other.
    
    Much inspiration for this module was drawn from:
    https://github.com/amueller/word_cloud and
    http://peekaboo-vision.blogspot.com/2012/11/a-wordcloud-in-python.html
    
    This all-Python implementation is indeed rather sluggish -- a rewrite
    might be necessary in the future, but this is definitely functional
    and is a great starting point.
    '''


    def __init__(self, weighted_terms, output_filename, 
                 image_height=400, image_width=800):
        self.weighted_terms = weighted_terms
        self.output_filename = output_filename
        self.image_height = image_height
        self.image_width = image_width

    
    def query_integral_image(self, integral_image, size_x, size_y):
        '''
        This is adapted from the word cloud GitHub project mentioned
        in the above comments.
        '''
        x_coord = integral_image.shape[0]
        y_coord = integral_image.shape[1]
        hits = 0
        # count possible locations
        for i in xrange(x_coord - size_x):
            for j in xrange(y_coord - size_y):
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
        for i in xrange(x_coord - size_x):
            for j in xrange(y_coord - size_y):
                area = integral_image[i, j] \
                    + integral_image[i + size_x, j + size_y]
                area -= integral_image[i + size_x, j] \
                    + integral_image[i, j + size_y]
                if not area:
                    hits += 1
                    if hits == goal:
                        return (i, j)
        
        
    def generate_word_cloud(self, num_terms_to_visualize=50, margin=5):
        '''
        In simple terms, we size each term proportional to its weight
        and then try to find a spot on the canvas where it fits. We 
        first build a black & white image and then redraw in color, 
        as this is faster than calculating and drawing in color the first time.
        '''
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
                print "Term '{0}' has weight {1}.".format(term, weight)
                return 0
        # reduce the term list down to length num_terms_to_visualize
        if num_terms_to_visualize < len(self.weighted_terms):
            term_list = self.weighted_terms[:num_terms_to_visualize] 
        else:
            term_list = self.weighted_terms
        # sort term list by weights
        term_list.sort(key=lambda pair: pair[1], reverse=True)
        
        # create black&white image
        black_white_image = Image.new("L", (self.image_width, 
                                            self.image_height))
        draw = ImageDraw.Draw(black_white_image)
        integral = numpy.zeros((self.image_height, self.image_width),
                               dtype=numpy.uint32)
        image_array = numpy.asarray(black_white_image) 
        font_sizes, term_positions, term_orientations = [], [], []
        # set font_size to "large enough" value
        font_size = 200
        
        for term, weight in term_list:
            font_size = min(font_size, int(100 * numpy.log(weight + 100)))
            while True:
                font = ImageFont.truetype(FONT_PATH, font_size)
                # optionally rotate orientation
                orientation = random.choice([None, Image.ROTATE_90])
                transposed_font = ImageFont.TransposedFont(font,
                                                        orientation=orientation)
                draw.setfont(transposed_font)
                # get size of box for current term
                term_box_size = draw.textsize(term)
                # query_integral_image to get possible places for current term
                location_result = self.query_integral_image(integral, 
                                                    term_box_size[1] + margin,
                                                    term_box_size[0] + margin)
                # if there are results or font_size hits 0, we're done
                if location_result is not None or font_size == 0:
                    break
                else:
                    font_size -= 1
            # if font_size hits 0, we cannot draw anymore
            if font_size == 0:
                break
            # set x and y coords for placing term and then draw it
            x_coord, y_coord = numpy.array(location_result) + margin // 2
            draw.text((y_coord, x_coord), term, fill="white")
            term_positions.append((x_coord, y_coord))
            term_orientations.append(orientation)
            font_sizes.append(font_size) 

            image_array = numpy.asarray(black_white_image)
            temp_sum = numpy.cumsum(image_array[x_coord:, y_coord:], axis=1)
            partial_integral = numpy.cumsum(temp_sum, axis=0)
            # paste recomputed part into old image
            if x_coord > 0:
                if y_coord > 0:
                    partial_integral += (integral[x_coord-1, y_coord:]
                                         - integral[x_coord-1, y_coord-1])
                else:
                    partial_integral += integral[x_coord-1, y_coord:]
            if y_coord > 0:
                partial_integral += integral[x_coord:, y_coord-1][:, numpy.newaxis]
            integral[x_coord:, y_coord:] = partial_integral
        
        # now redraw entire image in color
        color_image = Image.new("RGB", (self.image_width, self.image_height),
                                "white")
        color_draw = ImageDraw.Draw(color_image)
        # build a list of big tuples with all the needed info for each term
        terms = [term for term, weight in term_list]
        term_data = zip(terms, font_sizes, term_positions, term_orientations)
        for term, font_size, term_position, term_orientation in term_data:
            font = ImageFont.truetype(FONT_PATH, font_size)
            transposed_font = ImageFont.TransposedFont(font, 
                                                orientation=term_orientation)
            color_draw.setfont(transposed_font)
            color_draw.text((term_position[1], term_position[0]),
                             term, fill="hsl(%d" % random.randint(0, 255)
                             + ", 80%, 50%)")
        
        #black_white_image = ImageOps.invert(black_white_image)
        # display image
        #black_white_image.show()
        color_image.show()
        # save image to file
        #black_white_image.save(self.output_filename)
        color_image.save(self.output_filename)
