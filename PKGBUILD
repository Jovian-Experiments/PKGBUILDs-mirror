# Maintainer: Holo Team
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=alsa-ucm-conf
pkgver=1.2.16.1
pkgrel=1.1 # Holo: remove Jupiter symlink, fix DualSense haptics
pkgdesc="ALSA Use Case Manager configuration (and topologies)"
arch=(any)
url="https://alsa-project.org/"
license=(BSD-3-Clause)
source=(
  $url/files/pub/lib/$pkgname-$pkgver.tar.bz2{,.sig}

  # Holo: Apply workaround to fix native DualSense support in games
  # Upstream issue reported at https://github.com/alsa-project/alsa-ucm-conf/issues/677
  # Patch provided at https://github.com/alsa-project/alsa-ucm-conf/issues/677#issuecomment-3716152027
  # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1476
  'USB-Audio-DualSense-PS5-Add-support-for-haptic-feedb.patch'::'https://github.com/cristicc/alsa-ucm-conf/commit/48af6eac3651158b14a045661df71a4bb655c41f.patch'
)
sha512sums=('df25a29afc3b87347fa89f3fe60ebda68068acdaf68e081b58455ebee319c21e82af4076ba1f10781ba620a9e8efa6e65db27c5989d63a429d44a715dbd1d460'
            'SKIP'
            '2aabbd96ea21f370e56788fcde490fd665d8939c173d24c0c264d0c2f89209aa48c3091ccdf9e1d58e66b05e7cc2a284e9c905159db8457e2cc7fec5ee0a71df')
b2sums=('753e1775cd99c0f6289507d04760c7a87ead4a0d029a817aa3e6083a30eae123859a91432511f1e5f4daa25ddee960e8f3be130586a2761ee95bf4af40a76a13'
        'SKIP'
        '11cef3767c11f7da417a565a6f70fa7e8c4c6e6a02bb759213b66af7037d6f596195c62ea391e3c8cac75eabcdcf6f57964545afce410413d6d57771a3d38e5b')
validpgpkeys=('F04DF50737AC1A884C4B3D718380596DA6E59C91') # ALSA Release Team (Package Signing Key v1) <release@alsa-project.org>

prepare() {
  # Holo: Apply workaround to fix native DualSense support in games
  patch -d $pkgname-$pkgver -Np1 -i "${srcdir}/USB-Audio-DualSense-PS5-Add-support-for-haptic-feedb.patch"
}

package() {
  cd $pkgname-$pkgver
  install -vdm 755 "$pkgdir/usr/share/alsa/"
  cp -av ucm2 "$pkgdir/usr/share/alsa/"
  install -vDm 644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -vDm 644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -vDm 644 ucm2/README.md -t "$pkgdir/usr/share/doc/$pkgname/ucm2"

  # Holo: there missmatch between the kernel driver, firmware module and ucm
  # sequence needed. Drop the symlink, so our custom ucm gets picked.
  #
  # XXX: Add bug link/number once we have one with all the details.
  rm "$pkgdir/usr/share/alsa/ucm2/conf.d/acp5x/Valve-Jupiter-1.conf"
}
