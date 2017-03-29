from setuptools import setup

setup(
    name = "spiffy-test-app",
    version = "1.0",
    author = "Kale Franz",
    author_email = "kale@franz.io",
    license = "BSD",
    packages=[
        'spiffy_test_app',
    ],
    entry_points={
        'console_scripts': [
            "spiffy-test-app=spiffy_test_app:main",
            "spiffy-test-helper = spiffy_test_app:helper",
        ],
    },
    zip_safe=False,
)
