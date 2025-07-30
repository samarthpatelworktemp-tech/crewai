#!/usr/bin/env python
import sys
from marketing.crew import MarketingPostsCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'customer_domain': 'titan.co.in',
        'project_description': """
Titan, a leading lifestyle brand in India, aims to enhance brand engagement for its premium watch segment among urban millennials and Gen Z audiences. This project focuses on designing a creative, omni-channel marketing strategy that blends storytelling, influencer marketing, and experiential digital campaigns. 

Customer Domain: Lifestyle and Consumer Products (Watches)
Project Overview: Build an engaging marketing campaign to increase awareness and desirability of Titan’s premium watch collections, including designing presentation assets to pitch the campaign effectively, and saving the final PPT using available tools.
"""
    }
    MarketingPostsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'customer_domain': 'titan.co.in',
        'project_description': """
Titan, a leading lifestyle brand in India, aims to enhance brand engagement for its premium watch segment among urban millennials and Gen Z audiences. This project focuses on designing a creative, omni-channel marketing strategy that blends storytelling, influencer marketing, and experiential digital campaigns. 

Customer Domain: Lifestyle and Consumer Products (Watches)
Project Overview: Build an engaging marketing campaign to increase awareness and desirability of Titan’s premium watch collections, including designing presentation assets to pitch the campaign effectively, and saving the final PPT using available tools.
"""
    }

    try:
        MarketingPostsCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")