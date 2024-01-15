# Author : Clayton Craft <clayton@igalia.com>
# Maintainer : Manuel A. Fernandez Montecelo <mafm@igalia.com>

pkgname='holo-zram-swap'
pkgver=0.2
pkgrel=0
pkgdesc='Configures ZRAM swap'
arch=('any')
license=('LGPL2.1')
url='https://gitlab.steamos.cloud/holo/holo'
source=(
  'zram-generator.conf'
  'zswap-disable.conf'
)
sha256sums=('8434fa1700fe86b566eb95331d8bfffe104785597c43f797612b1d8eb63f2530'
            '15079234c4bbf5c94160495d7311ebe541e5fd0bad829ed5bfaa64cc4d512163')

package() {
  depends=('zram-generator')
  install -Dm644 zram-generator.conf -t "$pkgdir/usr/lib/systemd"
  install -Dm644 zswap-disable.conf -t "$pkgdir/usr/lib/tmpfiles.d"
}
