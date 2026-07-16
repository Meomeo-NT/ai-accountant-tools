import { test, expect } from '@playwright/test';

test('homepage loads with key sections', async ({ page }) => {
  await page.goto('/');

  await expect(page).toHaveTitle(/AI Accountant Tools/i);
  await expect(page.getByRole('heading', { name: /AI Accountant Tools/i })).toBeVisible();
  await expect(page.getByRole('link', { name: /Browse Workflows/i })).toBeVisible();
  await expect(page.getByRole('link', { name: /Explore Tools/i })).toBeVisible();
});
