#  SPDX-License-Identifier: LGPL-2.1+

# Maintainer: Emil Velikov <emil.l.velikov@gmail.com>

pkgname='jupiter-resolved-nomdns'
pkgver=1.0
pkgrel=1
pkgdesc="Holo tmpfiles.d rules for accessing DMI info"
arch=('any')
license=('LGPL2.1')
source=('00-disable-mdns.conf')
sha256sums=('9e1d19e154bb15464e64c6e3c8be80f39323cefd60124df033fdc6895537be1b')

package() {
  # Disable the resolved mdns since it clashes with the avahi one that we use
  # with the devkit service.
  install -Dt "$pkgdir/usr/lib/systemd/resolved.conf.d/" -m644 "$srcdir/00-disable-mdns.conf"
}
