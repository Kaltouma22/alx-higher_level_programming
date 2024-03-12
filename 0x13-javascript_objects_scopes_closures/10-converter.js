#!/usr/bin/node
exports.converter = function (base) {
  if (base === 0) {
    return '';
  }
  return this.converter(Math.floor(base / 10)) + (base % 10);
};
