""" algocollection - linear search for element in array
    Copyright (C) 2020 Raymond Mendelovits

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>. """


class Job(object):

    """ helper class to store and sort items """
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = end - start

    def __lt__(self, other):
        # One might mistakenly use
        # return self.duration < other.duration
        # but a short job can block two jobs
        # One might also mistakenly use
        # return self.start < other.start
        # but an early job might run long
        # the below works because of the
        # copy paste principle
        return self.end < other.end
