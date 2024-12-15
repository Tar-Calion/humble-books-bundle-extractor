import unittest
from bs4 import BeautifulSoup
from extractor.book import Book
from extractor.books_extractor import BooksExtractor


class TestBooksExtractor(unittest.TestCase):

    def setUp(self):
        self.extractor = BooksExtractor()
        with open('tests/resources/bundle-info.html', 'r', encoding='utf-8') as html_file:
            self.html_content = html_file.read()

    def test_extract(self):

        expected_books = [
            Book("The Cloud Data Lake",
                 "Rukmani Gopalan",
                 "More organizations than ever understand the importance of data lake architectures for deriving value from their data. Building a robust, scalable, and performant data lake remains a complex proposition, however, with a buffet of tools and options that need to work together to provide a seamless end-to-end pipeline from data to insights. This book provides a concise yet comprehensive overview on the setup, management, and governance of a cloud data lake. Author Rukmani Gopalan, a product management leader and data enthusiast, guides data architects and engineers through the major aspects of working with a cloud data lake, from design considerations and best practices to data format optimizations, performance optimization, cost management, and governance. Learn the benefits of a cloud-based big data strategy for your organization. Get guidance and best practices for designing performant and scalable data lakes. Examine architecture and design choices, and data governance principles and strategies. Build a data strategy that scales as your organizational and business needs increase. Implement a scalable data lake in the cloud. Use cloud-based advanced analytics to gain more value from your data",
                 None,
                 ["EPUB", "PDF"],
                 None,
                 "01.01.2021",
                 "Humble Tech Book Bundle: AWS, Azure, and Google Cloud Development by O'Reilly"),
            Book("Building Serverless Applications on Knative",
                 "Evan Anderson",
                 "Explore the theory and practice of designing and writing serverless applications using examples from the Knative project. With this practical guide, mid-level to senior application developers and team managers will learn when and why to target serverless platforms when developing microservices or applications. Along the way, you'll also discover warning signs that suggest cases when serverless might cause you more trouble than joy. Drawing on author Evan Anderson's 15 years of experience developing and maintaining applications in the cloud, and more than 6 years of experience with serverless platforms at scale, this book acts as your guide into the high-velocity world of serverless application development. You'll come to appreciate why Knative is the most widely adopted open source serverless platform available. With this book, you will:",
                 None,
                 ["EPUB", "PDF"],
                 None,
                 "01.01.2021",
                 "Humble Tech Book Bundle: AWS, Azure, and Google Cloud Development by O'Reilly"),
            Book("Learning Serverless",
                 "Jason Katzer",
                 "Whether your company is considering serverless computing or has already made the decision to adopt this model, this practical book is for you. Author Jason Katzer shows early and mid-career developers what's required to build and ship maintainable and scalable services using this model. With this book, you'll learn how to build a modern production system in the cloud, viewed through the lens of serverless computing. You'll discover how serverless can free you from the tedious task of setting up and maintaining systems in production. You'll also explore new ways to level up your careerand design, develop, and deploy with confidence. In three parts, this book includes: The Path to Production: Examine the ins and outs of distributed systems, microservices, interfaces, and serverless architecture and patterns. The Tools: Dive into monitoring, observability and alerting, logging, pipelines, automation, and deployment. Concepts: Learn how to design security and privacy, how to manage quality through testing and staging, and how to plan for failure",
                 None,
                 ["EPUB", "MOBI", "PDF"],
                 None,
                 "01.01.2021",
                 "Humble Tech Book Bundle: AWS, Azure, and Google Cloud Development by O'Reilly"),
            Book("Migrating to AWS: A Manager's Guide",
                 "Jeff Armstrong",
                 "Bring agility, cost savings, and a competitive edge to your business by migrating your IT infrastructure to AWS. With this practical book, executive and senior leadership and engineering and IT managers will examine the advantages, disadvantages, and common pitfalls when moving your company's operations to the cloud. Author Jeff Armstrong brings years of practical hands-on experience helping dozens of enterprises make this corporate change. You'll explore real-world examples from many organizations that have made -- or attempted to make -- this wide-ranging transition. Once you read this guide, you'll be better prepared to evaluate your migration objectively before, during, and after the process in order to ensure success. Learn the benefits and drawbacks of migrating to AWS, including the risks to your business and technology. Begin the process by discovering the applications and servers in your environment. Examine the value of AWS migration when building your business case. Address your operational readiness before you migrate. Define your AWS account structure and cloud governance controls. Create your migration plan in waves of servers and applications. Refactor applications that will benefit from using more cloud native resources",
                 None,
                 ["EPUB", "MOBI", "PDF"],
                 None,
                 "01.01.2021",
                 "Humble Tech Book Bundle: AWS, Azure, and Google Cloud Development by O'Reilly"),
            Book("Low-Code AI",
                 "Gwendolyn Stripling",
                 "Take a data-first and use-case-driven approach with. Low-Code AI. to understand machine learning and deep learning concepts. This hands-on guide presents three problem-focused ways to learn no-code ML using AutoML, low-code using BigQuery ML, and custom code using scikit-learn and Keras. In each case, you'll learn key ML concepts by using real-world datasets with realistic problems. Business and data analysts get a project-based introduction to ML/AI using a detailed, data-driven approach: loading and analyzing data; feeding data into an ML model; building, training, and testing; and deploying the model into production. Authors Michael Abel and Gwendolyn Stripling show you how to build machine learning models for retail, healthcare, financial services, energy, and telecommunications. You'll learn how to: Distinguish between structured and unstructured data and the challenges they present. Visualize and analyze data. Preprocess data for input into a machine learning model. Differentiate between the regression and classification supervised learning models. Compare different ML model types and architectures, from no code to low code to custom training. Design, implement, and tune ML models. Export data to a GitHub repository for data management and governance",
                 None,
                 ["EPUB", "PDF"],
                 None,
                 "01.01.2021",
                 "Humble Tech Book Bundle: AWS, Azure, and Google Cloud Development by O'Reilly"),
        ]
        actual_books = self.extractor.extract(self.html_content)
        for i in range(len(actual_books)):
            self.assertEqual(actual_books[i].title, expected_books[i].title)
            self.assertEqual(actual_books[i].author, expected_books[i].author)
            self.assertEqual(expected_books[i].description, actual_books[i].description)
            self.assertEqual(actual_books[i].year, expected_books[i].year)
            self.assertEqual(
                actual_books[i].formats, expected_books[i].formats)
            self.assertRegex(
                actual_books[i].purchase_date, r'\d{2}\.\d{2}\.\d{4}')
            self.assertEqual(actual_books[i].source, expected_books[i].source)


if __name__ == '__main__':
    unittest.main()
