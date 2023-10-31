# Maintainer: Your Name <youremail@domain.com>
pkgname=foxnetstatsd
pkgver=1.3
pkgrel=2
pkgdesc="Foxnet stats daemon"
arch=(any)
depends=(python3 python-psutil python-aiohttp nvme-cli)
makedepends=(git openssh)
source=(wheel-foxnetstatsd
        foxnetstatsd.service
        git+ssh://git@gitlab.steamos.cloud/jupiter/foxnetstatsd.git#tag="$pkgver")
sha256sums=('d3195621e665c490f77694fe23ce2448c190c436b4521593d0aee7c54d7f9299'
            '34d9355de1ce9744f1b6d8cc31cce24447d895b1b0de901d3845e3c696a2cc55'
            'SKIP')

package() {
  install -D -m644 -t "$pkgdir"/usr/python/foxnetstatsd/ foxnetstatsd/*.py
  install -D -m644 wheel-foxnetstatsd "$pkgdir"/etc/sudoers.d/wheel-foxnetstatsd

  install -D -m755 -t "$pkgdir"/usr/bin/ foxnetstatsd/foxnet-stats-daemon

  install -D -m644 foxnetstatsd.service "$pkgdir"/etc/systemd/system/foxnetstatsd.service

  mkdir -p -m755 "$pkgdir"/etc/systemd/system/sound.target.wants
  mkdir -p -m755 "$pkgdir"/etc/systemd/system/multi-user.target.wants
}
