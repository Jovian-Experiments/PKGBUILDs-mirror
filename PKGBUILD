# Author : Clayton Craft <clayton@igalia.com>

pkgname='steamos-systemreport'
pkgver=0.1
pkgrel=2
pkgdesc='System report collection tool'
arch=('any')
license=('LGPL2.1')
url='https://gitlab.steamos.cloud/holo/holo'
source=(steamos-systemreport)
sha256sums=('d494e0134b2644978f05c0486ae5ef5a70304c82801fc7e44d7779beec2e55a1')

package() {
  depends=(pciutils upower usbutils)
  install -Dm755 steamos-systemreport -t "$pkgdir"/usr/bin/
}
