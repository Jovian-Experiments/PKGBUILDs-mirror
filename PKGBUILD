# Maintainer: Holo Team
# Contributor: David Runge <dvzrv@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=alsa-ucm-conf
pkgver=1.2.14
pkgrel=2.4 # Holo: remove Jupiter symlink, backport DualSense UCM and fix DualSense haptics
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

  # Holo: Apply workaround to fix native DualSense support in games
  # Upstream issue reported at https://github.com/alsa-project/alsa-ucm-conf/issues/677
  # Patch provided at https://github.com/alsa-project/alsa-ucm-conf/issues/677#issuecomment-3716152027
  # Part of https://gitlab.steamos.cloud/holo-team/tasks/-/issues/1476
  'USB-Audio-DualSense-PS5-Add-support-for-haptic-feedb.patch'::'https://github.com/cristicc/alsa-ucm-conf/commit/48af6eac3651158b14a045661df71a4bb655c41f.patch'
)
sha512sums=('a224e890919306bdcd606dfb873b089950c9fa89f24c02947692ee8ab1a05c419f2a8dc174440d17c8a9575cab293806630f2cb43d74677f7ef0d956b7883dc5'
            'SKIP'
            '2c328ded0d7b72530328d510914381921f7d0477e599f989cb025b4eb1e842b0ce6c0bbce65d3558a1f89c8ac4611cf1f533acd4a0f2cf6c1adfe88e7c88c488'
            '299170a809ab9a63372bf7ee0e2185f831f69555d207eb9e9f500cc51fc57ceb0e05ebc4f2e87d7e7c1aea05772411a1766983a8774f1b521c7806795ec4ed17'
            '9e962c464a2d2d7ec55e35dbdb1f5429d043861098641b634eeda3006310d2346acc2dd8db061f965940358e588efdd97fcf36eab1d5cac8fb5d453595e84490')
b2sums=('cbb4b81db7670207cac5b85ba9cd4d9df93e4aca573da4caffe0f1e0386a9685b837e58b7ed85ddcfecf3c0f2469e706833dad6f0ef020440c943aa41520f8f0'
        'SKIP'
        '3c53e0d627021e0d086ce13144b72f6b08b6df09d99a4278ab8cfd5e1d3ba542c04e95483b41557f2c0cc62331718fe059bba46c18c2fc99b26d25f152047e99'
        '5960187de1dcd99071b6108d2f130356a66df87b54c9f267a61082a39f5802466cae7b5dc1b786ed9affdb6b4e76d33afa5f2867d3ae0b806c5ea12db51b10d1'
        '7524c1213a0545fc7dcb6426382457f53eeaaa522cfef7b3a07bd833dd57974a9f345829c583694defe08073744d6453f94cc01ecd594bc1489e222046e4acf5')
validpgpkeys=('F04DF50737AC1A884C4B3D718380596DA6E59C91') # ALSA Release Team (Package Signing Key v1) <release@alsa-project.org>

prepare() {
  # https://github.com/alsa-project/alsa-ucm-conf/issues/550
  # https://gitlab.archlinux.org/archlinux/packaging/packages/alsa-ucm-conf/-/issues/2
  patch -d $pkgname-$pkgver -Np1 -i "${srcdir}/010-alsa-ucm-conf-fix-acp3x-alc5682-max98357.patch"

  # Holo: backport of upstream patch
  patch -d $pkgname-$pkgver -Np1 -i "${srcdir}/usb-audio-add-support-for-dualsense.patch"

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
