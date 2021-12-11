from setuptools import setup, find_packages

setup(
    name='guri',
    version='0.0.1',
    description='Event-Driven Framework for Highly-Scalable Realtime Data Loads',
    author='Paul Herrera',
    author_email='pauljherrera@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    keywords='real-time event-driven',
    packages=find_packages(exclude=('tests', 'deploys', 'scripts')),
    install_requires=[
        'pika'
    ]
)
