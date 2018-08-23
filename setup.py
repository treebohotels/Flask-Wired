from setuptools import setup, find_packages


def get_version():
    return '0.1'


setup(
    name='Flagon',
    version=get_version(),
    license='BSD',
    author='Karthikkannan Maruthamuthu',
    author_email='karthikkannan@gmail.com',
    maintainer='Karthikkannan Maruthamuthu',
    maintainer_email='karthikkannan@gmail.com',
    description='Package for Flask wiring.',

    packages=find_packages(exclude=['tests', 'sample_app']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.6',

    install_requires=[
        'Flask==1.0.2',
        'Flask-Script==2.0.6',
        'Flask-Migrate==2.2.1',
        'flask-marshmallow==0.9.0',
        'Flask-SQLAlchemy==2.3.2',
        'marshmallow-sqlalchemy==0.14.1',
        'psycopg2==2.7.5',
    ],
    entry_points={
    },
    test_suite="tests",

    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Flagon',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
