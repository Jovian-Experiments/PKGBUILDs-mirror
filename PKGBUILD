# Maintainer: Holo Team
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=alsa-ucm-conf
pkgver=1.2.14
pkgrel=2.2 # Holo: remove Jupiter symlink and backport DualSense UCM
pkgdesc="ALSA Use Case Manager configuration (and topologies)"
arch=(any)
url="https://alsa-project.org/"
license=(BSD-3-Clause)
source=(
  $url/files/pub/lib/$pkgname-$pkgver.tar.bz2{,.sig}
  '010-alsa-ucm-conf-fix-acp3x-alc5682-max98357.patch'::'https://github.com/alsa-project/alsa-ucm-conf/commit/25f519f66c3e496b21ca1ad83ebc6114dfaa9fc3.patch'

  # Holo: Backport https://github.com/alsa-project/alsa-ucm-conf/commit/36a111ad007f2f424e6b00155970aaf07e86cee3
  # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1476
  # This will be included in alsa-ucm-conf 1.2.15 and newer
  'usb-audio-add-support-for-dualsense.patch'::'https://github.com/alsa-project/alsa-ucm-conf/commit/36a111ad007f2f424e6b00155970aaf07e86cee3.patch'
)
sha512sums=('a224e890919306bdcd606dfb873b089950c9fa89f24c02947692ee8ab1a05c419f2a8dc174440d17c8a9575cab293806630f2cb43d74677f7ef0d956b7883dc5'
            'SKIP'
            'd5eb3c3b96f6616e39f6d551e1a5fb888f15e1d940785a9d546134298ff46b5dbbb3354a39c885126c8db3dcfcd350ed4195b6930e9ca5846923abf4c8bf0cc6'
            '4f0bb826e8f5f3ec74ce24147d1c0c15d945971aa7ea020500044db83e3bf9baddfffd46d298c635be836a0b6d51490c3bd77ffa33b1b98e8702e9b911e9f0c4')
b2sums=('cbb4b81db7670207cac5b85ba9cd4d9df93e4aca573da4caffe0f1e0386a9685b837e58b7ed85ddcfecf3c0f2469e706833dad6f0ef020440c943aa41520f8f0'
        'SKIP'
        'cc6e37135301187d42c6f54950c7ba9d86217dd04d2726a4123b0a357981172fa43605c6ed6034f2df5fa648b2802e4c3ef62e877040ee870a03fda7f13f1b8d'
        'fe6720b4fef9e79af1007f5da4c4130bba1b2eb43bc336764fde2eb6467c62acf7bfb9bf453580cfb5c7eb8824abafdd002d9546a845e50dae6de39053842cd0')
validpgpkeys=('F04DF50737AC1A884C4B3D718380596DA6E59C91') # ALSA Release Team (Package Signing Key v1) <release@alsa-project.org>

prepare() {
  # https://github.com/alsa-project/alsa-ucm-conf/issues/550
  # https://gitlab.archlinux.org/archlinux/packaging/packages/alsa-ucm-conf/-/issues/2
  patch -d $pkgname-$pkgver -Np1 -i "${srcdir}/010-alsa-ucm-conf-fix-acp3x-alc5682-max98357.patch"

  # Holo: backport of upstream patch
  patch -d $pkgname-$pkgver -Np1 -i "${srcdir}/usb-audio-add-support-for-dualsense.patch"
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
