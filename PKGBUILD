# Maintainer: Your Name <youremail@domain.com>
pkgname=foxnetstatsd
pkgver=1.1
pkgrel=2
pkgdesc="Foxnet stats daemon"
arch=(any)
depends=(python3 python-psutil python-aiohttp nvme-cli)
makedepends=(git)
source=(nvme_stats
        foxnetstatsd.service
        git+ssh://git@gitlab.internal.steamos.cloud/jupiter/foxnetstatsd.git#tag="$pkgver")
sha256sums=('6285185681303c5fda7102a20ec7f9302b62759593bf2502c5c5467214148643'
            '34d9355de1ce9744f1b6d8cc31cce24447d895b1b0de901d3845e3c696a2cc55'
            'SKIP')

package() {
  install -D -m644 -t "$pkgdir"/usr/python/foxnetstatsd/ foxnetstatsd/*.py
  install -D -m644 nvme_stats "$pkgdir"/etc/sudoers.d/nvme_stats

  install -D -m755 -t "$pkgdir"/usr/bin/ foxnetstatsd/foxnet-stats-daemon

  install -D -m644 foxnetstatsd.service "$pkgdir"/etc/systemd/system/foxnetstatsd.service

  mkdir -p -m755 "$pkgdir"/etc/systemd/system/sound.target.wants
  mkdir -p -m755 "$pkgdir"/etc/systemd/system/multi-user.target.wants
}
