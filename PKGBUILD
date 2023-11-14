# Maintainer: John Schoenick <johns@valvesoftware.com>
pkgname=foxnetstatsd
pkgver=1.4
pkgrel=1
pkgdesc="Foxnet stats daemon"
arch=(any)
depends=(python3 python-psutil python-aiohttp nvme-cli)
makedepends=(git openssh)
source=(wheel-foxnetstatsd
        foxnetstatsd.service
        git+ssh://git@gitlab.steamos.cloud/jupiter/foxnetstatsd.git#tag="$pkgver")
sha256sums=('8faa8a10d832b483886ce0d59e2d513f3288fe96bdd56e1599004b83a4da08dc'
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
