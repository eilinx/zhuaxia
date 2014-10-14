from setuptools import setup, find_packages
import glob
setup(
    name = 'zhuaxia',
    version = '2.0.0',
    install_requires=[ 'requests','mutagen' ],
    packages = find_packages(),
    package_data={'zhuaxia':['conf/*.conf']},
    #data_files=[('conf',glob.glob('conf/*.*'))],
    include_package_data= True,
    zip_safe=False,
    scripts=['zx'],
    author='Kai Yuan',
    author_email='kent.yuan@gmail.com',
    platforms=['POSIX'],
    keywords='xiami mp3 download',
    url='https://github.com/sk1418/zhuaxia',
    description='a cli tool to download mp3 from xiami.com',
    long_description="""
        a cli tool to download mp3 from xiami.com
    """,
)
