# Author : Clayton Craft <clayton@igalia.com>

pkgname='steamos-systemreport'
pkgver=0.2
pkgrel=1
pkgdesc='System report collection tool'
arch=('any')
license=('LGPL2.1')
url='https://gitlab.steamos.cloud/holo/holo'
source=(steamos-systemreport)
sha256sums=('d84c407463ecc473493fc2c7b695300e7171bb99c9b4b6a6f530414553ed854c')

package() {
  depends=(pciutils upower usbutils)
  install -Dm755 steamos-systemreport -t "$pkgdir"/usr/bin/
}
