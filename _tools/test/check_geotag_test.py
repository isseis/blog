#! /usr/bin/python3

import unittest
import check_geotag

class TestCheckGeoTag(unittest.TestCase):

    def testIsGeoTaggedT(self):
        self.assertTrue(check_geotag.is_geotagged('geotagged.jpg'))

    def testIsGeoTaggedF(self):
        self.assertFalse(check_geotag.is_geotagged('nogeotagged.jpg'))

    def testFindGeoTaggedFiles(self):
        self.assertCountEqual(
                check_geotag.find_geotagged_files([
                    'geotagged.jpg', 'nogeotagged.jpg']),
                ['geotagged.jpg'])

    def testIsJpegFile(self):
        self.assertTrue(check_geotag.is_jpeg_file('foo/bar.jpg'))
        self.assertTrue(check_geotag.is_jpeg_file('/foo/bar.jpeg'))
        self.assertTrue(check_geotag.is_jpeg_file('/foo/bar.JPG'))
        self.assertTrue(check_geotag.is_jpeg_file('foo/bar.JPEG'))
        self.assertFalse(check_geotag.is_jpeg_file('bar.png'))
        self.assertFalse(check_geotag.is_jpeg_file('/foo/bar.jpegx'))
        self.assertFalse(check_geotag.is_jpeg_file('/foo/bar.jpeg.old'))

    def testFfilterJpegFiles(self):
        self.assertCountEqual(
                check_geotag.filter_jpeg_files([
                    '/foo/bar.png',
                    '/foo/bar.jpg',
                    ]),
                ['/foo/bar.jpg'])


if __name__ == '__main__':
    unittest.main()
