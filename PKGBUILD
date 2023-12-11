# Author : Clayton Craft <clayton@igalia.com>

pkgname='holo-zram-swap'
pkgver=0.1
pkgrel=0
pkgdesc='Configures ZRAM swap'
arch=('any')
license=('LGPL2.1')
url='https://gitlab.steamos.cloud/holo/holo'
source=(
  'zram-generator.conf'
  'zswap-disable.conf'
)
sha256sums=('4fbc09bc0f4679a68bb64e2e795f9de9c48e23aff521402dc793933d1671c1bf'
            '15079234c4bbf5c94160495d7311ebe541e5fd0bad829ed5bfaa64cc4d512163')

package() {
  depends=('zram-generator')
  install -Dm644 zram-generator.conf -t "$pkgdir/usr/lib/systemd"
  install -Dm644 zswap-disable.conf -t "$pkgdir/usr/lib/tmpfiles.d"
}
